# Generated by Django 3.2.9 on 2021-11-24 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20211121_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
