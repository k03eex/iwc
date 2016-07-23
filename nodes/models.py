from django.db import models

# Create your models here.

class Node(models.Model):
    node_id = models.CharField(max_length=255)

    def __str__(self):
        return self.node_id

class Sensor(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    aci = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    light = models.FloatField()
    pressure = models.FloatField()


class NodeGPS(models.Model):
    node_id = models.ForeignKey(Node)
    gps_latitude = models.FloatField()
    gps_longitude = models.FloatField()
    gps_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    gps_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class NodeConfig(models.Model):
    node_id = models.ForeignKey(Node)
    node_configuration = models.TextField()
    config_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    config_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
