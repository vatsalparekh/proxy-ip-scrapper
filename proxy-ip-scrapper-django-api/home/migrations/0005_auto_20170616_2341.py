# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170616_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipdata',
            old_name='last_modified',
            new_name='last_updated',
        ),
    ]
