# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_locationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='location',
            field=models.CharField(max_length=45),
        ),
    ]
