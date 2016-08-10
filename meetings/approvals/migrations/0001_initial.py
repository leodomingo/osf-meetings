# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('view_approval', 'Can view approval'),),
            },
        ),
    ]
