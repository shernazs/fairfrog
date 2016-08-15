# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-15 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawledProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webshop', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=2000)),
                ('img', models.CharField(max_length=2000)),
                ('price', models.FloatField()),
                ('sizes', models.TextField()),
                ('tags', models.TextField()),
            ],
        ),
    ]