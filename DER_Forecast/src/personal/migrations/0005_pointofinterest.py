# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20160320_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
    ]
