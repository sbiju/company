# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20170612_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]