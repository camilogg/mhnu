# Generated by Django 3.2.6 on 2021-09-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0004_alter_slider_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='order',
            field=models.PositiveSmallIntegerField(unique=True, verbose_name='order'),
        ),
    ]
