# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='书名')),
                ('auth', models.CharField(max_length=54, verbose_name='作者')),
                ('zishu', models.IntegerField(blank=True, null=True, verbose_name='字数')),
                ('sale', models.FloatField(blank=True, null=True, verbose_name='售价')),
                ('img', models.URLField(blank=True, null=True, verbose_name='图片')),
                ('daoyan', models.TextField(verbose_name='导言')),
                ('mulu', models.TextField(verbose_name='导言')),
                ('tejia', models.FloatField(blank=True, null=True, verbose_name='活动价')),
                ('is_tui', models.BooleanField(default=False, verbose_name='推荐')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
            ],
            options={
                'verbose_name': '书名',
                'verbose_name_plural': '书名',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Bookcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connt', models.TextField(verbose_name='内容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
            ],
            options={
                'verbose_name': '书的评论',
                'verbose_name_plural': '书的评论',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Bookfenlei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='分类名')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('sattus', models.BooleanField(default=False, verbose_name='状态')),
                ('level', models.IntegerField(default=999, verbose_name='等级')),
            ],
            options={
                'verbose_name': '书分类',
                'verbose_name_plural': '书分类',
                'ordering': ['-id'],
            },
        ),
    ]