from datetime import datetime

from django.utils.translation import ugettext as _

from . import tasks


def run_import_job_action(modeladmin, request, queryset):
    for instance in queryset:
        tasks.logger.info(f"Importing {instance.pk} dry-run: False")
        tasks.run_import_job.delay(instance.pk, dry_run=False)


run_import_job_action.short_description = _("Perform import")


def run_import_job_action_dry(modeladmin, request, queryset):
    for instance in queryset:
        tasks.logger.info(f"Importing {instance.pk} dry-run: True")
        tasks.run_import_job.delay(instance.pk, dry_run=True)


run_import_job_action_dry.short_description = _("Perform dry import")


def run_export_job_action(modeladmin, request, queryset):
    for instance in queryset:
        instance.processing_initiated = datetime.now()
        instance.save()
        tasks.run_export_job.delay(instance.pk)


run_export_job_action.short_description = _("Run export job")
