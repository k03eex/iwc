from django.db import models
from django.contrib.postgres.fields import ArrayField
#from django.contrib.postgres.forms import SimpleArrayField


class Node(models.Model):
    '''Table contains nodes, it will be used as ForeignKey for other tables'''
    node_id = models.CharField(max_length=255)

    def __str__(self):
        return self.node_id

class Sensor(models.Model):
    '''Database table for sensor parameters'''
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    sensor_created = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    light_red = models.IntegerField(null=True, blank=True)
    light_green = models.IntegerField(null=True, blank=True)
    light_blue = models.IntegerField(null=True, blank=True)


class ACI(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    aci_created = models.DateTimeField(null=True, blank=True)
    aci = ArrayField(models.FloatField())

class NodeMemoryGPS(models.Model):
    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    mem_gps_created = models.DateTimeField(null=True, blank=True)
    gps_latitude = models.FloatField(null=True, blank=True)
    gps_longitude = models.FloatField(null=True, blank=True)
    memory_total = models.FloatField(null=True, blank=True)
    memory_free = models.FloatField(null=True, blank=True)

class NodeConfig(models.Model):
    WINDOW_CHOICES = (
        (1, 'Hamming'),
        (2, 'Hanning'),
        (3, 'Blackman'),
        (0, 'Default')
    )

    RECORD_TIME = (
        (1.5, '1.5 mins'),
        (2.0, '2 mins'),
        (2.5, '2.5 mins'),
        (3.0, '3 mins'),
        (0, 'Default')
    )

    node_id = models.ForeignKey(Node)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    record_time = models.FloatField(choices=RECORD_TIME, default=0)
    record_interval = models.IntegerField(default=0, help_text = "")
    lower_frequency = models.IntegerField(default=0, help_text = "Please, enter between 1 and 256")
    upper_frequency = models.IntegerField(default=0, help_text = "Please, enter between 1 and 256")
    window = models.IntegerField(choices=WINDOW_CHOICES, default=0)
    measurement_interval = models.IntegerField(default=0, help_text = "")
