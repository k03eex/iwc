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
#import necessary modules to work with URLs and admin panel
from django.conf.urls import include, url
from django.contrib import admin
#import views to associate with urls
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'), #the main page
    url(r'^admin/', include(admin.site.urls)), #redirect to built-in admin panel
    url(r'^about/$', views.about, name='about'), #about page
    url(r'^home/$', views.home, name='home'), #home page
    url(r'^nodes/', include('nodes.urls', namespace='nodes')), #redirect to app url
    url(r'^nodes/gps_json/$', views.get_gps_json, name='gps_json'), #get GPS json data
    url(r'^api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')), #redirect to rest_framework auth
    url(r'^api/v1/nodes/', include('nodes.url_api', namespace='nodes_api')), #redirect to app API url
]
