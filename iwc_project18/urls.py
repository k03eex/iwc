"""iwc_project18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.about, name='about'),
    url(r'^home/$', views.home, name='home'),
    url(r'^nodes/', include('nodes.urls', namespace='nodes')),
    url(r'^nodes/gps_json/$', views.get_gps_json, name='gps_json'),
    url(r'^api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    url(r'^api/v1/nodes/', include('nodes.url_api', namespace='nodes_api')),
]
