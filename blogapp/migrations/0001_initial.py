# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-14 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=40, verbose_name='标题')),
                ('content', models.TextField(null=True, verbose_name='正文')),
                ('pub_time', models.DateTimeField(null=True, verbose_name='日期')),
            ],
        ),
    ]