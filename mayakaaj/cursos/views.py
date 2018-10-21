from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import curso


# Create your views here.
def temario(request):
    Cursos=curso.objects.all()
    context = {
        'titulo_pagina': 'Temario',          
        'Cursos':Cursos
    }
    return render (request,'html/temario.html',context)