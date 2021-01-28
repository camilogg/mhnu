from django import forms
from django.contrib import admin
from django.core.cache import cache

from . import models, admin_actions


class JobWithStatusMixin:
    def job_status_info(self, obj):
        job_status = cache.get(f'{self.direction}_job_status_{obj.pk}')
        if job_status:
            return job_status
        else:
            return obj.job_status


@admin.register(models.ImportJob)
class ImportJobAdmin(JobWithStatusMixin, admin.ModelAdmin):
    direction = "import"
    list_display = (
        "model",
        "job_status_info",
        "file",
        "change_summary",
        "imported",
        'created_by',
        'modified_by'
    )
    readonly_fields = (
        "job_status_info",
        "change_summary",
        'processing_initiated',
        "imported",
        "errors",
        'created_by',
        'modified_by'
    )
    exclude = ("job_status",)

    list_filter = ("model", "imported")
    actions = (
        admin_actions.run_import_job_action,
        admin_actions.run_import_job_action_dry,
    )


class ExportJobForm(forms.ModelForm):
    class Meta:
        model = models.ExportJob
        exclude = ("site_of_origin",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["resource"].widget = forms.Select(
            choices=self.instance.get_resource_choices()
        )


@admin.register(models.ExportJob)
class ExportJobAdmin(JobWithStatusMixin, admin.ModelAdmin):
    direction = "export"
    form = ExportJobForm
    list_display = (
        "model",
        "app_label",
        "file",
        "job_status_info",
        'created_by',
        'modified_by'
    )
    readonly_fields = (
        "job_status_info",
        "app_label",
        "model",
        "file",
        "processing_initiated",
        'created_by',
        'modified_by'
    )
    exclude = ("job_status",)
    list_filter = ("model",)
    actions = (admin_actions.run_export_job_action,)
    raw_id_fields = ('collection_code',)

    def has_add_permission(self, request):
        return False
