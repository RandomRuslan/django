# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='answer',
            table='Answer',
        ),
        migrations.AlterModelTable(
            name='question',
            table='Question',
        ),
    ]