from django.db import models
from gestion_usuarios.models import Usuario
# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Deporte')

    def __str__(self):
        return self.nombre

class Lugar(models.Model):
    TIPOS = (
        (0,'PRIVADO'),
        (1,'PUBLICO'),
    )
    nombre = models.CharField(max_length=150,verbose_name='Nombre')
    tipo = models.IntegerField(choices=TIPOS,verbose_name='Tipos')
    latitud = models.FloatField()
    longitud = models.FloatField()
    web = models.URLField(blank=True,null=True)

class Evento(models.Model):
    DIFICULTADES = (
        (0,'INDIFERENTE'),
        (1,'PRINCIPIANTE'),
        (2,'INTERMEDIO'),
        (3,'AVANZADO')
    )
    creador = models.ForeignKey(Usuario)
    fecha = models.DateTimeField(auto_now=True)
    plazas = models.IntegerField()
    dificultad = models.IntegerField(choices=DIFICULTADES,verbose_name='Nivel')
    deporte = models.ForeignKey(Deporte)
    lugar = models.ForeignKey(Lugar)

class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario)
    fecha = models.DateTimeField(auto_now=True)
    descripcion = models.TextField()
    evento = models.ForeignKey(Evento)

class ParticipantesEvento(models.Model):
    evento = models.ForeignKey(Evento)
    jugadores = models.ManyToManyField(Usuario)


