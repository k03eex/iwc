from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ListCreateNode.as_view(),
        name='node_api_list'),
    url(r'^(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNode.as_view(),
        name='node_api_detail'),
#################SENSORS##################################
    url(r'^sensors/$',
        views.ListCreateSensors.as_view(),
        name='sensors_api_list'),
    url(r'^sensors/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroySensors.as_view(),
        name='sensors_api_detail'),

    url(r'^(?P<node_pk>\d+)/sensors/$',
        views.ListCreateSensor.as_view(),
        name='sensor_api_list'),
    url(r'^(?P<node_pk>\d+)/sensors/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroySensor.as_view(),
        name='sensor_api_detail'),
#####################ACI###############################
    url(r'^aci/$',
        views.ListCreateACIs.as_view(),
        name='aci-s_api_list'),
    url(r'^aci/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyACIs.as_view(),
        name='aci-s_api_detail'),

    url(r'^(?P<node_pk>\d+)/aci/$',
        views.ListCreateACI.as_view(),
        name='aci_api_list'),
    url(r'^(?P<node_pk>\d+)/aci/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyACI.as_view(),
        name='aci_api_detail'),
###################GPS###################################
    url(r'^gps/$',
        views.ListCreateNodesGPS.as_view(),
        name='nodes_gps_api_list'),
    url(r'^gps/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNodesGPS.as_view(),
        name='nodes_gps_api_detail'),

    url(r'^(?P<node_pk>\d+)/gps/$',
        views.ListCreateNodeGPS.as_view(),
        name='node_gps_api_list'),
    url(r'^(?P<node_pk>\d+)/gps/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNodeGPS.as_view(),
        name='node_gps_api_detail'),
#######################CONFIG################################
    url(r'^config/$',
        views.ListCreateNodesConfig.as_view(),
        name='nodes_config_api_list'),
    url(r'^config/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNodesConfig.as_view(),
        name='nodes_config_api_detail'),

    url(r'^(?P<node_pk>\d+)/config/$',
        views.ListCreateNodeConfig.as_view(),
        name='node_config_api_list'),
    url(r'^(?P<node_pk>\d+)/config/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNodeConfig.as_view(),
        name='node_config_api_detail'),
######################MEMORY#######################################
    url(r'^memory/$',
        views.ListCreateNodesMemory.as_view(),
        name='nodes_memory_api_list'),
    url(r'^memory/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNodesMemory.as_view(),
        name='nodes_memory_api_detail'),

    url(r'^(?P<node_pk>\d+)/memory/$',
        views.ListCreateNodeMemory.as_view(),
        name='node_memory_api_list'),
    url(r'^(?P<node_pk>\d+)/memory/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNodeMemory.as_view(),
        name='node_memory_api_detail'),
]
