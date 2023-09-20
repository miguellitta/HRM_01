from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    candidatos = [
        {
            'nombre': 'Julian',
            'profesion': 'Abogado',
            'ciudad': 'Cordoba',
            'portada': {
                'imagen': "img/img_avatar-3.png"
            }
        },
        {
            'nombre': 'Diana',
            'profesion': 'Contadora',
            'ciudad': 'Rosario',
            'portada': {
                'imagen': "img/img_avatar-2.png"
            }
        },
        {
            'nombre': 'Sebastián',
            'profesion': 'Ingeniero Industrial',
            'ciudad': 'Pergamino',
            'portada': {
                'imagen': "img/img_avatar-3.png"
            }
        },
        {
            'nombre': 'Rocio',
            'profesion': 'Economista',
            'ciudad': 'Puerto Madryn',
            'portada': {
                'imagen': "img/img_avatar-1.png"
            }
        },
        {
            'nombre': 'Juan Pablo',
            'profesion': 'Panadero',
            'ciudad': 'Junín',
            'portada': {
                'imagen': "img/img_avatar-3.png"
            }
        },
        {
            'nombre': 'Sofia',
            'profesion': 'Administrativa',
            'ciudad': 'Ramallo',
            'portada': {
                'imagen': "img/img_avatar-2.png"
            }
        },
    ]
    return render(request, "recruitment/index.html", {'candidatos': candidatos})

def profiles(request):
    return render(request, "recruitment/profiles.html")

def recruiters(request, inicio):
    reclutadores = [
        {
            'nombre': 'Matias',
            'profesion': 'Reclutador IT',
            'ciudad': 'San Miguel',
            'portada': {
                'imagen': "img/img_avatar-3.png"
            }
        },
        {
            'nombre': 'Florencia',
            'profesion': 'Reclutadora',
            'ciudad': 'Ushuaia',
            'portada': {
                'imagen': "img/img_avatar-2.png"
            }
        },
        {
            'nombre': 'Martin',
            'profesion': 'Reclutador',
            'ciudad': 'Zarate',
            'portada': {
                'imagen': "img/img_avatar-3.png"
            }
        },
        {
            'nombre': 'Rocio',
            'profesion': 'Reclutadora',
            'ciudad': 'Berazategui',
            'portada': {
                'imagen': "img/img_avatar-1.png"
            }
        },
        {
            'nombre': 'Nicolas',
            'profesion': 'Reclutador IT',
            'ciudad': 'Villa Constitución',
            'portada': {
                'imagen': "img/img_avatar-3.png"
            }
        },
        {
            'nombre': 'Victoria',
            'profesion': 'Reclutadora',
            'ciudad': 'Ramallo',
            'portada': {
                'imagen': "img/img_avatar-2.png"
            }
        },
    ]
    return render(request, "recruitment/recruiters.html", {'reclutadores': reclutadores})

def signin(request):
    return render(request, "recruitment/signin.html")