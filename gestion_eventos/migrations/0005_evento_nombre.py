# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_eventos', '0004_auto_20160226_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=150, default='Evento de futbol 7'),
            preserve_default=False,
        ),
    ]
