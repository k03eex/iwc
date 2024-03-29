from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

from rest_framework import generics

from . import serializers
from . import forms
from . import models


def node_detail(request, node_pk):
    node = "Node" + str(node_pk)
    return render(request, "nodes/node_detail.html", {'node': node, 'node_id': node_pk})
'''
@login_required
def node_config(request):
    form = forms.NodeConfigForm
    if request.method == 'POST':
        form = forms.NodeConfigForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Configuration successfully submitted!")
            return HttpResponseRedirect(reverse('nodes:config'))
    return render(request, 'nodes/nodeconfig.html', {'form': form})

'''
###############################################################################
############################-------API------###################################
###############################################################################

class ListCreateNode(generics.ListCreateAPIView):
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer

class RetrieveUpdateDestroyNode(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer

##############################SENSOR############################################

class ListCreateSensors(generics.ListCreateAPIView):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer

class RetrieveUpdateDestroySensors(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer


class ListCreateSensor(generics.ListCreateAPIView):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer

    def get_queryset(self):
        return self.queryset.filter(node_id=self.kwargs.get('node_pk')).order_by('timestamp')

    def perform_create(self, serializer):
        node = get_object_or_404(
            models.Node, pk=self.kwargs.get('node_pk'))
        serializer.save(node_id=node)

class RetrieveUpdateDestroySensor(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            node_id=self.kwargs.get('node_pk'),
            pk=self.kwargs.get('pk')
        )

#############################ACI################################################

class ListCreateACIs(generics.ListCreateAPIView):
    queryset = models.ACI.objects.all()
    serializer_class = serializers.ACISerializer

class RetrieveUpdateDestroyACIs(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ACI.objects.all()
    serializer_class = serializers.ACISerializer


class ListCreateACI(generics.ListCreateAPIView):
    queryset = models.ACI.objects.all()
    serializer_class = serializers.ACISerializer

    def get_queryset(self):
        return self.queryset.filter(node_id=self.kwargs.get('node_pk')).order_by('timestamp')

    def perform_create(self, serializer):
        node = get_object_or_404(
            models.Node, pk=self.kwargs.get('node_pk'))
        serializer.save(node_id=node)

class RetrieveUpdateDestroyACI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ACI.objects.all()
    serializer_class = serializers.ACISerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            node_id=self.kwargs.get('node_pk'),
            pk=self.kwargs.get('pk')
        )

##############################MEMORY-GPS###############################################

class ListCreateNodesMemoryGPS(generics.ListCreateAPIView):
    queryset = models.NodeMemoryGPS.objects.all()
    serializer_class = serializers.NodeMemoryGPSSerializer

class RetrieveUpdateDestroyNodesMemoryGPS(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeMemoryGPS.objects.all()
    serializer_class = serializers.NodeMemoryGPSSerializer

class ListCreateNodeMemoryGPS(generics.ListCreateAPIView):
    queryset = models.NodeMemoryGPS.objects.all()
    serializer_class = serializers.NodeMemoryGPSSerializer

    def get_queryset(self):
        return self.queryset.filter(node_id=self.kwargs.get('node_pk')).order_by('timestamp')

    def perform_create(self, serializer):
        node = get_object_or_404(
            models.Node, pk=self.kwargs.get('node_pk'))
        serializer.save(node_id=node)

class RetrieveUpdateDestroyNodeMemoryGPS(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeMemoryGPS.objects.all()
    serializer_class = serializers.NodeMemoryGPSSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            node_id=self.kwargs.get('node_pk'),
            pk=self.kwargs.get('pk')
        )

############################Config##############################################

class ListCreateNodesConfig(generics.ListCreateAPIView):
    queryset = models.NodeConfig.objects.all()
    serializer_class = serializers.NodeConfigSerializer


class RetrieveUpdateDestroyNodesConfig(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeConfig.objects.all()
    serializer_class = serializers.NodeConfigSerializer


class ListCreateNodeConfig(generics.ListCreateAPIView):
    serializer_class = serializers.NodeConfigSerializer

    def get_queryset(self):
        return models.NodeConfig.objects.filter(node_id=self.kwargs.get('node_pk')).order_by('timestamp')

    def perform_create(self, serializer):
        node = get_object_or_404(
            models.Node, pk=self.kwargs.get('node_pk'))
        serializer.save(node_id=node)

class RetrieveUpdateDestroyNodeConfig(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeConfig.objects.all()
    serializer_class = serializers.NodeConfigSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            node_id=self.kwargs.get('node_pk'),
            pk=self.kwargs.get('pk')
        )

class RetrieveNodeConfig(generics.RetrieveAPIView):
    queryset = models.NodeConfig.objects.all()
    serializer_class = serializers.NodeConfigSerializer

    def get_object(self, *args, **kwargs):
        return self.get_queryset().filter(node_id=self.kwargs.get('node_pk')).latest('timestamp')
