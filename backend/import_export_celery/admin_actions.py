from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from . import tasks
from .models import ExportJob


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
        instance.processing_initiated = timezone.now()
        instance.save()
        tasks.run_export_job.delay(instance.pk)


run_export_job_action.short_description = _("Run export job")


def create_export_job_action(modeladmin, request, queryset):
    if queryset:
        # arbitrary_obj = queryset.first()
        ej = ExportJob.objects.create(
            # app_label=arbitrary_obj._meta.app_label,
            # model=arbitrary_obj._meta.model_name,
            queryset=[obj.pk for obj in queryset],
            site_of_origin=request.scheme + "://" + request.get_host(),
        )
    url = reverse(
        'admin:{}_{}_change'.format(ej._meta.app_label, ej._meta.model_name),
        args=[ej.pk],
    )
    return redirect(url)


create_export_job_action.short_description = _('Export')
