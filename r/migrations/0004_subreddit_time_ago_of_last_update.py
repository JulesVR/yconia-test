# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0003_imageobject_id_nb'),
    ]

    operations = [
        migrations.AddField(
            model_name='subreddit',
            name='time_ago_of_last_update',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
