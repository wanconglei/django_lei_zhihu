# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('huati', '0011_auto_20171111_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenthuati',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='huati.Commenthuati'),
        ),
    ]
