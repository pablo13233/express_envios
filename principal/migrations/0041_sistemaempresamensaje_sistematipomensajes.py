# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-28 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0040_cliente_revenedor_creo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaEmpresamensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=1000)),
                ('fecha', models.DateField()),
                ('precio', models.FloatField()),
                ('pagado', models.BooleanField()),
                ('fecha_pago', models.DateField()),
            ],
            options={
                'db_table': 'sistema_empresamensaje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SistemaTipomensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_mensaje', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sistema_tipomensajes',
                'managed': False,
            },
        ),
    ]
