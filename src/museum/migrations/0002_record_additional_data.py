# Generated by Django 3.2.6 on 2021-08-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='additional_data',
            field=models.JSONField(blank=True, null=True, verbose_name='additional data'),
        ),
    ]
