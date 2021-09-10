from django.db import models
from django.utils.translation import gettext_lazy as _

from import_export.formats.base_formats import DEFAULT_FORMATS

from museum.models import CollectionCode, Record
from utils.models import Audit


class ExportJob(Audit):

    file = models.FileField(
        verbose_name=_('exported file'),
        upload_to='export-jobs',
        blank=False,
        null=False,
        max_length=255,
    )

    processing_initiated = models.DateTimeField(
        verbose_name=_('Have we started processing the file? If so when?'),
        null=True,
        blank=True,
        default=None,
    )

    job_status = models.CharField(
        verbose_name=_('Status of the job'),
        max_length=255,
        blank=True
    )

    format = models.CharField(
        verbose_name=_('Format of file to be exported'),
        max_length=255,
        choices=[(f.CONTENT_TYPE, f().get_title()) for f in DEFAULT_FORMATS],
        blank=False,
        null=True,
    )

    collection_code = models.ForeignKey(
        CollectionCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('collection code'),
        help_text=_('select the type of collection to export or leave it empty'
                    ' to export all records')
    )

    email_on_completion = models.BooleanField(
        verbose_name=_('Send me an email when this export job is complete'),
        default=True,
    )

    site_of_origin = models.TextField(
        _('site of origin'),
        max_length=255,
        default='',
    )

    queryset = models.JSONField(
        verbose_name=_('JSON list of pks to export'), blank=True, null=True
    )

    def get_queryset(self):
        queryset = Record.objects.all()
        if self.collection_code:
            queryset = queryset.filter(collection_code=self.collection_code)
        if self.queryset:
            queryset = queryset.filter(pk__in=self.queryset)
        return queryset

    class Meta:
        verbose_name = _('export job')
        verbose_name_plural = _('export jobs')
        db_table = 'export_job'

    def __str__(self):
        return _('Export job #{}').format(self.pk)
