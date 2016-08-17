# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('aci_created', models.DateTimeField(null=True, blank=True)),
                ('aci', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.FloatField())),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('node_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NodeConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('record_time', models.FloatField(choices=[(1.5, '1.5 mins'), (2.0, '2 mins'), (2.5, '2.5 mins'), (3.0, '3 mins'), (0, 'Default')], default=0)),
                ('record_interval', models.IntegerField(default=0)),
                ('lower_frequency', models.IntegerField(default=0, help_text='Please, enter between 1 and 256')),
                ('upper_frequency', models.IntegerField(default=0, help_text='Please, enter between 1 and 256')),
                ('window', models.IntegerField(choices=[(1, 'Hamming'), (2, 'Hanning'), (3, 'Blackman'), (0, 'Default')], default=0)),
                ('measurement_interval', models.IntegerField(default=0)),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.CreateModel(
            name='NodeMemoryGPS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('mem_gps_created', models.DateTimeField(null=True, blank=True)),
                ('gps_latitude', models.FloatField(null=True, blank=True)),
                ('gps_longitude', models.FloatField(null=True, blank=True)),
                ('memory_total', models.FloatField(null=True, blank=True)),
                ('memory_free', models.FloatField(null=True, blank=True)),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor_created', models.DateTimeField(null=True, blank=True)),
                ('temperature', models.FloatField(null=True, blank=True)),
                ('humidity', models.FloatField(null=True, blank=True)),
                ('pressure', models.FloatField(null=True, blank=True)),
                ('light_red', models.IntegerField(null=True, blank=True)),
                ('light_green', models.IntegerField(null=True, blank=True)),
                ('light_blue', models.IntegerField(null=True, blank=True)),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.AddField(
            model_name='aci',
            name='node_id',
            field=models.ForeignKey(to='nodes.Node'),
        ),
    ]
