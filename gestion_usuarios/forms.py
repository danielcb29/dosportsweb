#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from gestion_usuarios.models import Usuario

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ('username','first_name','last_name','email','password','fecha_nacimiento','genero',)
        widgets = {
            'password' : forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(),
        }