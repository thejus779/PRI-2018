# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-08 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180701_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%D/', verbose_name=''),
        ),
    ]
