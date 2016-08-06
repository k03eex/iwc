# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0003_auto_20160802_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aci',
            name='aci',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.FloatField()),
        ),
        migrations.AlterUniqueTogether(
            name='nodegps',
            unique_together=set([('node_id', 'gps_latitude', 'gps_longitude')]),
        ),
    ]
