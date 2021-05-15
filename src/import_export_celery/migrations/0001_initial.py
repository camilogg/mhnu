# Generated by Django 3.2.3 on 2021-05-15 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('museum', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date when the object was created', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='modified at')),
                ('file', models.FileField(max_length=255, upload_to='import-jobs', verbose_name='File to be imported')),
                ('processing_initiated', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Have we started processing the file? If so when?')),
                ('imported', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Has the import been completed? If so when?')),
                ('format', models.CharField(choices=[('text/csv', 'csv'), ('application/vnd.ms-excel', 'xls'), ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'xlsx'), ('text/tab-separated-values', 'tsv'), ('application/vnd.oasis.opendocument.spreadsheet', 'ods'), ('application/json', 'json'), ('text/yaml', 'yaml'), ('text/html', 'html')], max_length=255, verbose_name='Format of file to be imported')),
                ('change_summary', models.FileField(blank=True, null=True, upload_to='summaries', verbose_name='Summary of changes made by this import')),
                ('errors', models.TextField(blank=True, default='', null=True, verbose_name='errors')),
                ('job_status', models.CharField(blank=True, max_length=160, verbose_name='Status of the job')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importjob_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importjob_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'import job',
                'verbose_name_plural': 'import jobs',
            },
        ),
        migrations.CreateModel(
            name='ExportJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date when the object was created', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='modified at')),
                ('file', models.FileField(max_length=255, upload_to='export-jobs', verbose_name='exported file')),
                ('processing_initiated', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Have we started processing the file? If so when?')),
                ('job_status', models.CharField(blank=True, max_length=255, verbose_name='Status of the job')),
                ('format', models.CharField(choices=[('text/csv', 'csv'), ('application/vnd.ms-excel', 'xls'), ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'xlsx'), ('text/tab-separated-values', 'tsv'), ('application/vnd.oasis.opendocument.spreadsheet', 'ods'), ('application/json', 'json'), ('text/yaml', 'yaml'), ('text/html', 'html')], max_length=255, null=True, verbose_name='Format of file to be exported')),
                ('email_on_completion', models.BooleanField(default=True, verbose_name='Send me an email when this export job is complete')),
                ('site_of_origin', models.TextField(default='', max_length=255, verbose_name='site of origin')),
                ('queryset', models.JSONField(blank=True, null=True, verbose_name='JSON list of pks to export')),
                ('collection_code', models.ForeignKey(blank=True, help_text='select the type of collection to export or leave it empty to export all records', null=True, on_delete=django.db.models.deletion.SET_NULL, to='museum.collectioncode', verbose_name='collection code')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exportjob_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exportjob_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'export job',
                'verbose_name_plural': 'export jobs',
            },
        ),
    ]
