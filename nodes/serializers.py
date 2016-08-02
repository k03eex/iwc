from rest_framework import serializers

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
  #aci = serializers.ListField(child=serializers.FloatField(min_value=0, max_value=100))
  class Meta:
    fields = (
      'id',
      'node_id',
      'timestamp',
      'aci_created',
      'aci',
    )
    model = models.ACI

class NodeGPSSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
      'timestamp',
      'gps_created',
      'gps_latitude',
      'gps_longitude'
    )
    model = models.NodeGPS

class NodeConfigSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
      'timestamp',
      'node_configuration'
    )
    model = models.NodeConfig

class NodeMemorySerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
      'memory_total',
      'memory_free'
    )
    model = models.NodeMemory
