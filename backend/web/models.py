from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from utils.models import Audit


class Slider(Audit):
    name = models.CharField(_('name'), max_length=255)
    order = models.PositiveSmallIntegerField(_('order'), unique=True)
    image = models.ImageField(_('image'), upload_to='sliders')
    enabled = models.BooleanField(_('enabled'), default=True)

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
        ordering = ['order']

    def __str__(self):
        return self.name


class Member(Audit):
    name = models.CharField(_('name'), max_length=255)
    image = models.ImageField(_('image'), upload_to='members')
    position = models.CharField(_('position'), max_length=255)
    description = RichTextField(
        verbose_name=_('description'), blank=True, null=True
    )
    slug = AutoSlugField(
        populate_from='name', unique=True, blank=True, null=True
    )

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    def __str__(self):
        return self.name
