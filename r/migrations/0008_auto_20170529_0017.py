# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0007_imageobject_sub_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageobject',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imageobject',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
