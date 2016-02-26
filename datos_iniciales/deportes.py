from gestion_eventos.models import Deporte
from datos_iniciales.json_local import loc
from gestion_eventos.models import Lugar
deportes = [
    'Parapentismo', 'Aeromodelismo', 'Ala delta', 'Ultralivianos', 'Planeadores', 'Globos aerostáticos', 'Apnea',
    'Natación con aletas', 'Buceo', 'Hockey subacuático', 'Rugby subacuático', 'Pesca submarina', 'Orientacion',
    'Automovilismo deportivo','(Automovilismo deportivo) - Rallies colombiano','(Automovilismo deportivo) - Rallie Cross',
    '(Automovilismo deportivo) - Camper Cross', '(Automovilismo deportivo) - Velocidad', 'Ajedrez', 'Arquería', 'Bolos',
    'Ecuestre', 'Esgrima', 'Esquí Náutico', 'Futbol De Salon', 'Golf', 'Hapkido', 'Karts', 'Motociclismo','Motonautica', 'Squash',
    'Softbol', 'Tenis de mesa', 'Voleibol', 'Deportes Fuerzas Armadas', 'Deporte montaña y escalada','Coleo', 'Billar',
    'Nado sincronizado', 'Waterpolo', 'Badminton', 'Baloncesto', 'Canotaje', 'Balonmano', 'Hockey', 'Pentatlón moderno',
    'Vela', 'Tejo','Tiro Y Caza', 'Trampolín', 'Triatlón','Boccia', 'Baloncesto en Silla de Ruedas', 'Ciclismo Tandem',
    'Slalom', 'Tenis De Campo en Silla de Ruedas', 'Goalball', 'Powerlifting', 'Paracycling', 'Tenis en Silla de Ruedas',
    'Ciclismo','Ciclismo BMX','Ciclismo de montaña','Ciclismo en pista','Ciclismo en ruta','Fútbol','Natación','Tenis','Rugby'
]

def deportes_view(request):
    for d in deportes:
        Deporte(nombre=d).save()
    print('todos')

def inser_local(request):
    resultado = loc['results']['bindings']
    for r in resultado:
        Lugar(
            nombre=r['rdfs_label']['value'],
            latitud = r['geo_lat']['value'],
            longitud = r['geo_long']['value'],
            web = r['om_tieneEnlaceSIG']['value']
        ).save()
    print('todo bien')

