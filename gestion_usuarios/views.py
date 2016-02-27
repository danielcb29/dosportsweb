from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from gestion_usuarios.forms import UsuarioForm
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
from gestion_eventos.models import Evento,ParticipantesEvento,Usuario,Comentarios
# Create your views here.
def hello_world(request):
    return JsonResponse({0:'Hola mundo'})

def inicio(request):
    grupos = Group.objects.all()
    if not grupos:
        usuarios = Group(name='Usuarios')
        usuarios.save()
        usuarios.permissions.add(
            Permission.objects.get(codename='add_evento'),
            Permission.objects.get(codename='add_comentarios'),
            Permission.objects.get(codename='add_participantesevento'),
        )
    return render(request,'index.html',{

    })

@login_required
def inicio_login(request):
    return redirect('listar_eventos')

def crear_usuario(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(u.password)
            u.save()
            u.groups.add(Group.objects.get(name='Usuarios'))
            return redirect('inicio')
    return render(request,'register.html',{
        'form' : form
    })

@login_required
def mis_eventos(request):
    eventos = Evento.objects.filter(creador=request.user.id)
    return render(request,'listar_mis_eventos.html',{
        'eventos':eventos
    })

@login_required
def mis_suscripciones(request):
    suscripciones = [x.evento for x in ParticipantesEvento.objects.filter(jugadores__id__in=[request.user.id])]
    return render(request,'listar_mis_suscripciones.html',{
        'suscripciones':suscripciones
    })

@login_required
def mi_perfil(request):
    u = Usuario.objects.get(id=request.user.id)
    comentarios = Comentarios.objects.filter(usuario=request.user.id)[:3]
    return render(request,'mi_perfil.html',{
        'usuario': u,
        'comentarios': comentarios
    })

