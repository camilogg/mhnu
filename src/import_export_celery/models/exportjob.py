from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from import_export.formats.base_formats import DEFAULT_FORMATS

from museum.models import CollectionCode
from utils.models import Audit


class ExportJob(Audit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._content_type = None

    file = models.FileField(
        verbose_name=_("exported file"),
        upload_to="export-jobs",
        blank=False,
        null=False,
        max_length=255,
    )

    processing_initiated = models.DateTimeField(
        verbose_name=_("Have we started processing the file? If so when?"),
        null=True,
        blank=True,
        default=None,
    )

    job_status = models.CharField(
        verbose_name=_("Status of the job"),
        max_length=255,
        blank=True
    )

    format = models.CharField(
        verbose_name=_("Format of file to be exported"),
        max_length=255,
        choices=[(f.CONTENT_TYPE, f().get_title()) for f in DEFAULT_FORMATS],
        blank=False,
        null=True,
    )

    app_label = models.CharField(
        verbose_name=_("App label of model to export from"),
        max_length=160
    )

    model = models.CharField(
        verbose_name=_("Name of model to export from"),
        max_length=160
    )

    resource = models.CharField(
        verbose_name=_("Resource to use when exporting"),
        max_length=255,
        default=""
    )

    collection_code = models.ForeignKey(
        CollectionCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('collection code')
    )

    email_on_completion = models.BooleanField(
        verbose_name=_("Send me an email when this export job is complete"),
        default=True,
    )

    site_of_origin = models.TextField(
        _('site of origin'),
        max_length=255,
        default="",
    )

    def get_resource_class(self):
        if self.resource:
            return (
                self.get_content_type()
                    .model_class()
                    .export_resource_classes()[self.resource][1]
            )

    def get_content_type(self):
        if not self._content_type:
            self._content_type = ContentType.objects.get(
                app_label=self.app_label, model=self.model,
            )
        return self._content_type

    def get_queryset(self):
        if self.collection_code:
            return self.get_content_type().model_class().objects.filter(
                collection_code=self.collection_code
            )
        return self.get_content_type().model_class().objects.all()

    def get_resource_choices(self):
        return [
            (k, v[0]) for k, v in self.get_content_type()
                .model_class()
                .export_resource_classes()
                .items()
        ]

    class Meta:
        verbose_name = _('export job')
        verbose_name_plural = _('export jobs')

    def __str__(self):
        return _('{} export job #{}').format(self.model, self.pk)
