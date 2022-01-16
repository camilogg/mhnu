# Generated by Django 3.2.11 on 2022-01-16 07:59

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date when the object was created', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('order', models.PositiveSmallIntegerField(unique=True, verbose_name='order')),
                ('image', models.ImageField(upload_to='sliders', verbose_name='image')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slider_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slider_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
                'db_table': 'slider',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='date when the object was created', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.ImageField(upload_to='members', verbose_name='image')),
                ('position', models.CharField(max_length=255, verbose_name='position')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name', unique=True)),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
                'db_table': 'member',
            },
        ),
    ]
