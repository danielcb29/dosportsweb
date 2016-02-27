from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Usuario(User):
    GENEROS = (
        (0,'MASCULINO'),
        (1,'FEMENINO'),
    )
    PUNTOS = (
        (0,'DEFICIENTE'),
        (1,'MAL'),
        (2,'REGULAR'),
        (3,'BIEN'),
        (4,'MUY BIEN'),
        (5,'EXCELENTE'),

    )
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento',blank=True,null=True)
    genero = models.IntegerField(choices=GENEROS,verbose_name='Genero')
    puntuacion = models.IntegerField(choices=PUNTOS,verbose_name='Puntuación',blank=True,null=True)

    def edad(self):
        today = date.today()
        if self.fecha_nacimiento:
            return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return False