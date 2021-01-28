from datetime import datetime
import os

from celery import shared_task

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.cache import cache
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _

from import_export.formats.base_formats import DEFAULT_FORMATS

from . import models
from .model_config import ModelConfig

from celery.utils.log import get_task_logger
import logging

logger = logging.getLogger(__name__)

log = get_task_logger(__name__)

importables = getattr(settings, "IMPORT_EXPORT_CELERY_MODELS", {})


def change_job_status(job, direction, job_status, dry_run=False):
    if dry_run:
        job_status = _('[Dry run] ') + job_status
    else:
        job_status = job_status
    cache.set(direction + '_job_status_{}'.format(job.pk), job_status)
    job.job_status = job_status
    job.save()


def get_format(job):
    for format_type in DEFAULT_FORMATS:
        if job.format == format_type.CONTENT_TYPE:
            return format_type()


def _run_import_job(import_job, dry_run=True):
    change_job_status(import_job, _('import'), _('1/5 Import started'),
                      dry_run)
    if dry_run:
        import_job.errors = ''
    model_config = ModelConfig(**importables[import_job.model])
    import_format = get_format(import_job)
    try:
        data = import_job.file.read()
        if not import_format.is_binary():
            data = force_text(data, 'utf8')
        dataset = import_format.create_dataset(data)
    except UnicodeDecodeError as e:
        import_job.errors += _(
            'Imported file has a wrong encoding: {}'
        ).format(e) + "\n"
        change_job_status(
            import_job, _('import'), _('Imported file has a wrong encoding'),
            dry_run
        )
        import_job.save()
        return
    except Exception as e:
        import_job.errors += _('Error reading file: {}').format(e) + "\n"
        change_job_status(import_job, _('import'), _('Error reading file'),
                          dry_run)
        import_job.save()
        return
    change_job_status(import_job, _('import'), _('2/5 Processing import data'),
                      dry_run)

    class Resource(model_config.resource):
        def before_import_row(self, row, **kwargs):
            if 'row_number' in kwargs:
                row_number = kwargs['row_number']
                if row_number % 100 == 0 or row_number == 1:
                    change_job_status(
                        import_job,
                        _('import'),
                        _('3/5 Importing row {}/{}').format(
                            row_number, len(dataset)),
                        dry_run,
                    )
            return super(Resource, self).before_import_row(row, **kwargs)

    resource = Resource()

    if dry_run:
        result = resource.import_data(dataset, dry_run=dry_run)
    else:
        result = resource.import_data(dataset, dry_run=dry_run,
                                      raise_errors=True)
    change_job_status(
        import_job,
        _('import'),
        _('4/5 Generating import summary'),
        dry_run
    )
    for error in result.base_errors:
        import_job.errors += "\n%s\n%s\n" % (error.error, error.traceback)
    for line, errors in result.row_errors():
        for error in errors:
            import_job.errors += _('Line: {} - {}\n\t{}\n{}').format(
                line,
                error.error,
                ",".join(str(s) for s in error.row.values()),
                error.traceback,
            )

    if dry_run:
        ctx = {'result': result}
        summary = render_to_string('import_export_celery/import.html', ctx)

        import_job.change_summary.save(
            os.path.split(import_job.file.name)[1] + ".html",
            ContentFile(summary.encode("utf-8")),
        )
    else:
        import_job.imported = datetime.now()
    change_job_status(import_job, _('import'), _('5/5 Import job finished'),
                      dry_run)
    import_job.save()


@shared_task
def run_import_job(pk, dry_run=True):
    log.info('Importing {} dry-run {}'.format(pk, dry_run))
    import_job = models.ImportJob.objects.get(pk=pk)
    try:
        _run_import_job(import_job, dry_run)
    except Exception as e:
        import_job.errors += _('Import error {}').format(e) + "\n"
        change_job_status(import_job, _('import'), _('Import error'), dry_run)
        import_job.save()
        return


@shared_task
def run_export_job(pk):
    log.info("Exporting {}".format(pk))
    export_job = models.ExportJob.objects.get(pk=pk)
    resource_class = export_job.get_resource_class()
    queryset = export_job.get_queryset()
    qs_len = len(queryset)

    class Resource(resource_class):
        def __init__(self, *args, **kwargs):
            self.row_number = 1
            super().__init__(*args, **kwargs)

        def export_resource(self, *args, **kwargs):
            if self.row_number % 20 == 0 or self.row_number == 1:
                change_job_status(
                    export_job,
                    _('export'),
                    _('Exporting row {}/{}').format(self.row_number, qs_len),
                )
            self.row_number += 1
            return super(Resource, self).export_resource(*args, **kwargs)

    resource = Resource()

    data = resource.export(queryset)
    format = get_format(export_job)
    serialized = format.export_data(data)
    change_job_status(export_job, _('export'), _('Export complete'))
    filename = "{app}-{model}-{date}.{extension}".format(
        app=export_job.app_label,
        model=export_job.model,
        date=str(datetime.now()),
        extension=format.get_extension(),
    )
    if not format.is_binary():
        serialized = serialized.encode("utf8")
    export_job.file.save(filename, ContentFile(serialized))
    if export_job.email_on_completion:
        link = reverse("admin:{}_{}_change".format(
            export_job._meta.app_label,
            export_job._meta.model_name,
        ), args=[export_job.pk])
        send_mail(
            _('Django: Export job completed'),
            _(
                'Your export job on model {app_label}.{model} has completed. '
                'You can download the file at the following link:\n\n{link}'
            ).format(
                app_label=export_job.app_label,
                model=export_job.model,
                link=export_job.site_of_origin + link,
            ),
            settings.SERVER_EMAIL,
            [export_job.updated_by.email],
        )
