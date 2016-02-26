# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_eventos', '0002_auto_20160226_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='tipo',
            field=models.IntegerField(verbose_name='Tipos', default=1, choices=[(0, 'PRIVADO'), (1, 'PUBLICO')]),
        ),
    ]
