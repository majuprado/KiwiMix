from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, bem-vindo ao Kiwi Mix.")

def sobre(request):
    return HttpResponse("Esse é um app de Playlists.")