from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse

# Create your views here.
def auth_user(request):
    if request.method == 'POST':
        pass

    return JsonResponse({
        'respuesta': False
    })