# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-15 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
