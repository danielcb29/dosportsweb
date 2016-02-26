# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(verbose_name='Deporte', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('plazas', models.IntegerField()),
                ('dificultad', models.IntegerField(choices=[(0, 'INDIFERENTE'), (1, 'PRINCIPIANTE'), (2, 'INTERMEDIO'), (3, 'AVANZADO')], verbose_name='Nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(verbose_name='Nombre', max_length=150)),
                ('tipo', models.IntegerField(choices=[(0, 'PRIVADO'), (1, 'PUBLICO')], verbose_name='Tipos')),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('web', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantesEvento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('evento', models.ForeignKey(to='gestion_eventos.Evento')),
            ],
        ),
    ]
