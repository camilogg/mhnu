from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from import_export_celery.models import ExportJob, ImportJob

from .tasks import run_export_job, run_import_job


@receiver(post_save, sender=ExportJob)
def export_job_post_save(sender, instance, **_):
    if instance.format and not instance.processing_initiated:
        instance.processing_initiated = timezone.now()
        instance.save()
        transaction.on_commit(
            lambda: run_export_job.delay(instance.pk)
        )


@receiver(post_save, sender=ImportJob)
def import_job_post_save(sender, instance, **_):
    if not instance.processing_initiated:
        instance.processing_initiated = timezone.now()
        instance.save()
        transaction.on_commit(
            lambda: run_import_job.delay(instance.pk, dry_run=True)
        )
