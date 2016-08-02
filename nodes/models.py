from django.db import models
from django.contrib.postgres.fields import ArrayField


class Node(models.Model):
    node_id = models.CharField(max_length=255)

    def __str__(self):
        return self.node_id

class Sensor(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    sensor_created = models.DateTimeField()
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    light_red = models.IntegerField(null=True, blank=True)
    light_green = models.IntegerField(null=True, blank=True)
    light_blue = models.IntegerField(null=True, blank=True)


class ACI(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    aci_created = models.DateTimeField()
    aci = ArrayField(models.FloatField())


class NodeGPS(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    gps_created = models.DateTimeField()
    gps_latitude = models.FloatField(null=True, blank=True)
    gps_longitude = models.FloatField(null=True, blank=True)
    #gps_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class NodeConfig(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    node_configuration = models.TextField()
    #config_created = models.DateTimeField()
    #config_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class NodeMemory(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    memory_total = models.FloatField(null=True, blank=True)
    memory_free = models.FloatField(null=True, blank=True)
