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
      'aci',
      'temperature',
      'humidity',
      'light',
      'pressure'
    )
    model = models.Sensor

class NodeGPSSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
      'gps_latitude',
      'gps_longitude',
    )
    model = models.NodeGPS

class NodeConfigSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'node_id',
      'node_configuration',
    )
    model = models.NodeConfig
