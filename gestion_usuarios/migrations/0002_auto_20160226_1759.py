# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='puntuacion',
            field=models.IntegerField(null=True, blank=True, verbose_name='Puntuación', choices=[(0, 'DEFICIENTE'), (1, 'MAL'), (2, 'REGULAR'), (3, 'BIEN'), (4, 'MUY BIEN'), (5, 'EXCELENTE')]),
        ),
    ]
