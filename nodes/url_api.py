from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ListCreateNode.as_view(),
        name='node_api_list'),
    url(r'(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyNode.as_view(),
        name='node_api_detail'),

    url(r'(?P<node_pk>\d+)/sensors/$',
        views.ListCreateSensor.as_view(),
        name='sensor_api_list'),
    url(r'(?P<node_pk>\d+)/sensors/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroySensor.as_view(),
        name='sensor_api_detail'),

    url(r'^gps/$',
        views.ListCreateNodeGPS.as_view(),
        name='node_gps_api_list'),
    url(r'(?P<node_pk>\d+)/gps/$',
        views.RetrieveUpdateDestroyNodeGPS.as_view(),
        name='node_gps_api_detail'),

    url(r'^config/$',
        views.ListCreateNodeConfig.as_view(),
        name='node_config_api_list'),
    url(r'(?P<node_pk>\d+)/config/$',
        views.RetrieveUpdateDestroyNodeConfig.as_view(),
        name='node_config_api_detail'),
]
