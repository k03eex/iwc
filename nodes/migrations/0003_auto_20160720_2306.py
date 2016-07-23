# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_node_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('node_configuration', models.TextField()),
                ('config_created', models.DateTimeField(auto_now_add=True)),
                ('config_updated', models.DateTimeField(auto_now=True)),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.CreateModel(
            name='NodeGPS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gps_latitude', models.FloatField()),
                ('gps_longitude', models.FloatField()),
                ('gps_created', models.DateTimeField(auto_now_add=True)),
                ('gps_updated', models.DateTimeField(auto_now=True)),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.DeleteModel(
            name='NodeConfigLog',
        ),
    ]
