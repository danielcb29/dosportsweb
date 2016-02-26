"""dosports URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuarios/', include('gestion_usuarios.urls')),
    url(r'^eventos/', include('gestion_eventos.urls')),
    url(r'^rest/', include('rest.urls')),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'inicio'}, name='logout'),
    url(r'^$', 'gestion_usuarios.views.inicio',name='index'),
    url(r'^inicio$', 'gestion_usuarios.views.inicio_login',name='inicio'),
    url(r'^insertar-deportes', 'datos_iniciales.deportes.deportes_view'),
    url(r'^insertar-loc', 'datos_iniciales.deportes.inser_local'),
)

