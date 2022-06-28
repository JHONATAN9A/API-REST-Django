from django.shortcuts import render
from inmueblesList_App.models import Inmueble
from django.http import JsonResponse

# Funciones que permiten realizar la consulta a la DB
''' def inmueble_list(request):
    inmuebles = Inmueble.objects.all();
    data = {
        'inmuebles':list(inmuebles.values()),
        'mensaje':'Se retornan todos los inmuebles registrados',
    }
    
    return JsonResponse(data) '''