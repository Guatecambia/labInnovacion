# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 06:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('geoproyecto', '0006_auto_20180220_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='date voted',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 20, 6, 14, 45, 847183, tzinfo=utc), verbose_name='Fecha'),
        ),
    ]
