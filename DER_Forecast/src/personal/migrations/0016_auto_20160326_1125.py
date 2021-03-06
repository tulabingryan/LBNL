# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_forecastdatamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='cloudCover',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='datetime_ix',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='humidity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='solarForecast',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='temperature',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='windForecast',
            field=models.FloatField(),
        ),
    ]
