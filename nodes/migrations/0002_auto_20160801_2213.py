# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aci',
            name='aci',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.FloatField()),
        ),
    ]
