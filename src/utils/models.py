from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Audit(models.Model):
    """Audit Model
    AuditModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created_at (DateTime): Store the datetime the object was created.
        + modified_at (DateTime): Store the last datetime the object was
        modified.
        + created_by (ForeignKey): Store the user who created the object.
        + modified_by (ForeignKey): Store the user who modified the object.
    """

    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        help_text=_('date when the object was created'),
    )
    modified_at = models.DateTimeField(
        verbose_name=_('modified at'),
        auto_now=True,
        help_text=_('date when the object was modified'),
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_created_by',
        null=True, blank=True,
        verbose_name=_('created by'),
        help_text=_('user who created the object'),
    )
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_modified_by',
        null=True, blank=True,
        verbose_name=_('modified by'),
        help_text=_('user who performed the update'),
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super().save(*args, **kwargs)
