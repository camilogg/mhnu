from django import forms
from django.contrib import admin
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from . import models, admin_actions


class JobWithStatusMixin:
    direction = None

    def job_status_info(self, obj):
        job_status = cache.get(f'{self.direction}_job_status_{obj.pk}')
        if job_status:
            return job_status
        else:
            return obj.job_status

    job_status_info.short_description = _('status')


@admin.register(models.ImportJob)
class ImportJobAdmin(JobWithStatusMixin, admin.ModelAdmin):
    direction = 'import'
    list_display = (
        'id',
        'job_status_info',
        'file',
        'change_summary',
        'imported',
        'created_by',
        'modified_by'
    )
    readonly_fields = (
        'job_status_info',
        'change_summary',
        'processing_initiated',
        'imported',
        'errors',
        'created_by',
        'modified_by'
    )
    exclude = ('job_status',)

    list_filter = ('imported',)
    actions = (
        admin_actions.run_import_job_action,
        admin_actions.run_import_job_action_dry,
    )


class ExportJobForm(forms.ModelForm):
    class Meta:
        model = models.ExportJob
        exclude = ('site_of_origin',)


@admin.register(models.ExportJob)
class ExportJobAdmin(JobWithStatusMixin, admin.ModelAdmin):
    direction = 'export'
    form = ExportJobForm
    list_display = (
        'id',
        'file',
        'job_status_info',
        'created_by',
        'modified_by'
    )
    readonly_fields = (
        'job_status_info',
        'file',
        'processing_initiated',
        'created_by',
        'modified_by',
        'queryset'
    )
    exclude = ('job_status',)
    actions = (admin_actions.run_export_job_action,)
    autocomplete_fields = ('collection_code',)

    def has_add_permission(self, request):
        return False
