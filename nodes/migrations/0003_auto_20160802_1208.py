# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_auto_20160801_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aci',
            name='aci',
            field=django.contrib.postgres.fields.ArrayField(size=None, blank=True, base_field=models.FloatField()),
        ),
    ]
