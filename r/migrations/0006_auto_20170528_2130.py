# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 19:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0005_auto_20170528_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageobject',
            name='height',
        ),
        migrations.RemoveField(
            model_name='imageobject',
            name='width',
        ),
    ]
