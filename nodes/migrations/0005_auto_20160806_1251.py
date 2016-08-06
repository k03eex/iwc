# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0004_auto_20160806_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodememory',
            name='memory_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aci',
            name='aci_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nodegps',
            name='gps_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
