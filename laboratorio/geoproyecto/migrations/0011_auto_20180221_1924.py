# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoproyecto', '0010_auto_20180221_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Fotografia'),
        ),
    ]
