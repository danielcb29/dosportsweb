from django.db import models
from gestion_usuarios.models import Usuario
from django.utils import timezone

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
    tipo = models.IntegerField(choices=TIPOS,verbose_name='Tipos',default=1)
    latitud = models.FloatField()
    longitud = models.FloatField()
    web = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    DIFICULTADES = (
        (0,'INDIFERENTE'),
        (1,'PRINCIPIANTE'),
        (2,'INTERMEDIO'),
        (3,'AVANZADO')
    )
    nombre = models.CharField(max_length=150,verbose_name='Nombre del evento')
    creador = models.ForeignKey(Usuario)
    fecha = models.DateTimeField(verbose_name='Fecha del evento')
    plazas = models.IntegerField()
    dificultad = models.IntegerField(choices=DIFICULTADES,verbose_name='Nivel')
    deporte = models.ForeignKey(Deporte)
    lugar = models.ForeignKey(Lugar)

    def estado(self):
        print(self.fecha)
        print(timezone.datetime.now())
        if self.plazas_disponibles() == 0 or self.fecha < timezone.now():
            return False
        return True

    def plazas_disponibles(self):
        total_participantes = ParticipantesEvento.objects.get(evento=self).jugadores.all().count()
        return self.plazas - total_participantes

    def porcentaje(self):
        total_participantes = ParticipantesEvento.objects.get(evento=self).jugadores.all().count()
        return int((100*total_participantes)/self.plazas)

class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario)
    fecha = models.DateTimeField(auto_now=True)
    descripcion = models.TextField()
    evento = models.ForeignKey(Evento)

class ParticipantesEvento(models.Model):
    evento = models.ForeignKey(Evento)
    jugadores = models.ManyToManyField(Usuario)


