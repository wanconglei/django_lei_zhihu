# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coustmer', '0012_auto_20171110_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='zuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
