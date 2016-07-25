from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse

from rest_framework import generics

from . import serializers
from . import forms
from . import models
#from . import chartdata

#from .models import Node, NodeGps, NodeConfigLog

"""
def node_list(request, node_pk):
    nodes = Node.objects.all()
    return render(request, 'nodes/node_list.html', {'course': courses,
                                                       'email':email})
"""

def node_detail(request, node_pk):
    node = "Node" + str(node_pk)
    return render(request, "nodes/node_detail.html", {'node': node, 'node_id': node_pk})
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


###############################################################################
############################-------API------###################################
###############################################################################

class ListCreateNode(generics.ListCreateAPIView):
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer

class RetrieveUpdateDestroyNode(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer


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


class ListCreateNodeGPS(generics.ListCreateAPIView):
    queryset = models.NodeGPS.objects.all()
    serializer_class = serializers.NodeGPSSerializer


class RetrieveUpdateDestroyNodeGPS(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeGPS.objects.all()
    serializer_class = serializers.NodeGPSSerializer


class ListCreateNodeConfig(generics.ListCreateAPIView):
    queryset = models.NodeConfig.objects.all()
    serializer_class = serializers.NodeConfigSerializer


class RetrieveUpdateDestroyNodeConfig(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NodeConfig.objects.all()
    serializer_class = serializers.NodeConfigSerializer
