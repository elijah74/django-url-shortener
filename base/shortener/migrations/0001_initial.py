# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('link_url', models.URLField(max_length=255)),
                ('status', models.SmallIntegerField(choices=[(0, 'inactive'), (1, 'active')], default=1, verbose_name='status')),
            ],
            options={
                'verbose_name': 'shortener',
                'verbose_name_plural': 'shorteners',
            },
        ),
    ]
