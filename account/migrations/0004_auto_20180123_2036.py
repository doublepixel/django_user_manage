# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-23 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180122_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='brith',
            new_name='birth',
        ),
    ]
