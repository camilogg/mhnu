# Generated by Django 3.2.6 on 2021-09-06 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0003_slider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['order'], 'verbose_name': 'slider', 'verbose_name_plural': 'sliders'},
        ),
    ]