from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from gestion_eventos.forms import EventoForm
from gestion_usuarios.models import Usuario
from gestion_eventos.models import Evento,ParticipantesEvento,Comentarios
# Create your views here.
@login_required
def crear_evento(request):
    form = EventoForm()
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.creador = Usuario.objects.get(id=request.user.id)
            e.save()
            ParticipantesEvento(evento=e).save()
            return redirect('ver_evento',e.id)

    return render(request,'crear_evento.html',{
        'form': form
    })

@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request,'listar_eventos.html',{
        'eventos': eventos,
        'total' : eventos.count()
    })

@login_required
def ver_evento(request,id):
    try:
        evento = Evento.objects.get(id=id)
    except Exception:
        redirect('inicio')

    ids = [x.id for x in ParticipantesEvento.objects.get(evento=evento).jugadores.all()]
    suscrito=False
    if request.user.id in ids or request.user.id == evento.creador.id:
        suscrito = True

    comentarios  = Comentarios.objects.filter(evento=evento)

    return render(request,'ver_evento.html',{
        'evento': evento,
        'suscrito': suscrito,
        'comentarios' : comentarios
    })

@login_required
def suscribirse_evento(request,id_ev):
    usuario = Usuario.objects.get(id=request.user.id)
    ParticipantesEvento.objects.get(evento=id_ev).jugadores.add(usuario)
    return redirect('listar_eventos')

@login_required
def anular_suscripcion(request,id_ev):
    usuario = Usuario.objects.get(id=request.user.id)
    ParticipantesEvento.objects.get(evento=id_ev).jugadores.remove(usuario)
    return redirect('listar_eventos')

@login_required
def comentar(request,id_ev):
    evento = Evento.objects.get(id=id_ev)
    Comentarios(
        usuario=Usuario.objects.get(id=request.user.id),
        evento=evento,
        descripcion=request.POST['message']
    ).save()
    return redirect('ver_evento',id_ev)

@login_required
def calendario(request):
    return render(request,'calendar.html',{

    })