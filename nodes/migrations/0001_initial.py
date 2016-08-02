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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('aci_created', models.DateTimeField()),
                ('aci', django.contrib.postgres.fields.ArrayField(null=True, blank=True, size=None, base_field=models.FloatField())),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('node_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NodeConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('node_configuration', models.TextField()),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.CreateModel(
            name='NodeGPS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('gps_created', models.DateTimeField()),
                ('gps_latitude', models.FloatField(null=True, blank=True)),
                ('gps_longitude', models.FloatField(null=True, blank=True)),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.CreateModel(
            name='NodeMemory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('memory_total', models.FloatField(null=True, blank=True)),
                ('memory_free', models.FloatField(null=True, blank=True)),
                ('node_id', models.ForeignKey(to='nodes.Node')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor_created', models.DateTimeField()),
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
