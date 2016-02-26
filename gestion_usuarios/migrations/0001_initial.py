# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.IntegerField(choices=[(0, 'MASCULINO'), (1, 'FEMENINO')], verbose_name='Genero')),
                ('puntuacion', models.IntegerField(choices=[(0, 'DEFICIENTE'), (1, 'MAL'), (2, 'REGULAR'), (3, 'BIEN'), (4, 'MUY BIEN'), (5, 'EXCELENTE')], verbose_name='Puntuación')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
