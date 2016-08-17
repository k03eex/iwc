from rest_framework import serializers
#from drf_compound_fields.fields import ListField

from . import models

class NodeSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
    )
    model = models.Node

class SensorSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
      'timestamp',
      'sensor_created',
      'temperature',
      'humidity',
      'pressure',
      'light_red',
      'light_green',
      'light_blue'
    )
    model = models.Sensor

class ACISerializer(serializers.ModelSerializer):

  #aci = serializers.ListField(child=serializers.IntegerField())
  #aci_char = serializers.ListField(child=serializers.CharField(max_length=255))
  #test = serializers.ListField(child=serializers.CharField(max_length=255))

  class Meta:
    fields = (
      'id',
      'node_id',
      'timestamp',
      'aci_created',
      'aci',
    )
    model = models.ACI

class NodeMemoryGPSSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
      'timestamp',
      'mem_gps_created',
      'gps_latitude',
      'gps_longitude',
      'memory_total',
      'memory_free'
    )
    model = models.NodeMemoryGPS

class NodeConfigSerializer(serializers.ModelSerializer):
  lower_frequency = serializers.IntegerField(min_value=1, max_value=256, default=0, help_text="Please, enter between 1 and 256")
  upper_frequency = serializers.IntegerField(min_value=1, max_value=256, default=0, help_text="Please, enter between 1 and 256")
  class Meta:
    fields = (
      'id',
      'node_id',
      'timestamp',
      'record_time',
      'record_interval',
      'lower_frequency',
      'upper_frequency',
      'window',
      'measurement_interval',
    )
    model = models.NodeConfig
