from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('nav.html')
    context = {
        'titulo_pagina': 'Bienvenido a Mayakáaj'
    }
    return HttpResponse(template.render(context, request))

def cursos(request):
    template = loader.get_template('files/index.html')
    context = {
        'titulo_pagina': 'Cursos'
    }
    return HttpResponse(template.render(context, request))

def grupos(request):
    template = loader.get_template('files/index_grupo.html')
    context = {
        'titulo_pagina': 'Grupos'
    }
    return HttpResponse(template.render(context, request))
