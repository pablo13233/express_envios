# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-11 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_auto_20191211_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibocontenedor',
            name='recibo_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
