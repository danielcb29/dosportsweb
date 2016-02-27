from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from gestion_usuarios.forms import UsuarioForm
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
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
    return render(request,'listar_mis_eventos.html',{

    })