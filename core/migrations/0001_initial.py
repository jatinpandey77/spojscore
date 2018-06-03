# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=20)),
                ('users', models.IntegerField()),
                ('score', models.FloatField()),
            ],
        ),
    ]