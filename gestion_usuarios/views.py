from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from gestion_usuarios.forms import UsuarioForm
# Create your views here.
def hello_world(request):
    return JsonResponse({'Hola mundo'})

def inicio(request):
    return render(request,'index.html',{

    })

def crear_usuario(request):
    form = UsuarioForm()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        print('errror')
        print(form.errors)
    return render(request,'register.html',{
        'form' : form
    })