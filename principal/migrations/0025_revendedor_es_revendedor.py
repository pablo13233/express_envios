# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-01-08 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0024_remove_revendedor_es_revendedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='revendedor',
            name='es_revendedor',
            field=models.BooleanField(default=True),
        ),
    ]
