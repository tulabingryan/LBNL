# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 11:27
from __future__ import unicode_literals

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20160326_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='cloudCover',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='datetime_ix',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='humidity',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='solarForecast',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='temperature',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
        migrations.AlterField(
            model_name='forecastdatamodel',
            name='windForecast',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
