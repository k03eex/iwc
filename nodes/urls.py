from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.node_list, name='nodes'),
    url(r'^configuration/$', views.node_config, name='config'),
    url(r'(?P<node_pk>\d+)/$', views.node_detail, name='node'),
    #url(r'(?P<nodeid>\w+)/json_data/$', views.get_json_data, name='get_json')
]
