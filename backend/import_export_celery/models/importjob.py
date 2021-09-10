from django.db import models
from django.utils.translation import gettext_lazy as _

from import_export.formats.base_formats import DEFAULT_FORMATS

from utils.models import Audit


class ImportJob(Audit):
    file = models.FileField(
        verbose_name=_('File to be imported'),
        upload_to='import-jobs',
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

    imported = models.DateTimeField(
        verbose_name=_('Has the import been completed? If so when?'),
        null=True,
        blank=True,
        default=None,
    )

    format = models.CharField(
        verbose_name=_('Format of file to be imported'),
        max_length=255,
        choices=[(f.CONTENT_TYPE, f().get_title()) for f in DEFAULT_FORMATS],
    )

    change_summary = models.FileField(
        verbose_name=_('Summary of changes made by this import'),
        upload_to='summaries',
        blank=True,
        null=True,
    )

    errors = models.TextField(_('errors'), default='', blank=True, null=True)

    job_status = models.CharField(
        verbose_name=_('Status of the job'),
        max_length=160,
        blank=True,
    )

    class Meta:
        verbose_name = _('import job')
        verbose_name_plural = _('import jobs')
        db_table = 'import_job'

    def __str__(self):
        return _('Import job #{}').format(self.pk)
