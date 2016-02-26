#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from gestion_usuarios.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('puntuacion','is_staff','is_active','date_joined','objects',)