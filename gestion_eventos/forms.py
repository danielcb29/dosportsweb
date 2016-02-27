#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from gestion_eventos.models import Evento
from bootstrap3_datetime.widgets import DateTimePicker

class EventoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        #self.fields['fecha'].widget.attrs.update({'class': 'datetimepicker'})
        self.fields['fecha'].widget.attrs.update({'readonly': True})

    class Meta:
        model = Evento
        exclude = ('creador',)
        widgets = {
            'fecha': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}),

        }