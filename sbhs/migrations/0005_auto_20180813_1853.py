# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 13:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbhs', '0004_auto_20180810_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
