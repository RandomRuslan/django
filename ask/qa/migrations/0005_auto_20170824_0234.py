# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_auto_20170824_0232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='textss',
            new_name='text',
        ),
    ]
