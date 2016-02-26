# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_eventos', '0001_initial'),
        ('gestion_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantesevento',
            name='jugadores',
            field=models.ManyToManyField(to='gestion_usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='evento',
            name='creador',
            field=models.ForeignKey(to='gestion_usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='evento',
            name='deporte',
            field=models.ForeignKey(to='gestion_eventos.Deporte'),
        ),
        migrations.AddField(
            model_name='evento',
            name='lugar',
            field=models.ForeignKey(to='gestion_eventos.Lugar'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='evento',
            field=models.ForeignKey(to='gestion_eventos.Evento'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(to='gestion_usuarios.Usuario'),
        ),
    ]
