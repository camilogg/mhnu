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

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    def __str__(self):
        return self.name


class Post(Audit):
    name = models.CharField(_('name'), max_length=255)
    cover = models.ImageField(_('image'), upload_to='post_covers')
    summary = models.CharField(_('summary'), max_length=255)
    content = RichTextField(verbose_name=_('description'))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.name


class PostImage(Audit):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images'
    )
    name = models.CharField(_('name'), max_length=255, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='post_images')

    class Meta:
        verbose_name = _('post image')
        verbose_name_plural = _('post images')

    def __str__(self):
        return _('Image #{} of {}').format(self.id, self.post.name)
