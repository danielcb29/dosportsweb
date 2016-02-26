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


urlpatterns = patterns('gestion_eventos.views',
    url(r'^crear$','crear_evento',name='crear_evento' ),
    url(r'^listar$','listar_eventos',name='listar_eventos' ),
    url(r'^ver/(\d+)$','ver_evento',name='ver_evento' ),
    url(r'^suscribirse/(\d+)$','suscribirse_evento',name='suscribirse_evento'),
    url(r'^anular-sus/(\d+)$','anular_suscripcion',name='anular_suscripcion'),
    url(r'^comentar/(\d+)$','comentar',name='comentar'),

)

