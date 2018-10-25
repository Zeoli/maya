from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import curso,unidad,leccion


# Create your views here.
def temario(request):
    Cursos=curso.objects.all()
    Unidad = unidad.objects.all()
    Leccion = leccion.objects.all()
    context = {
        'titulo_pagina': 'Temario',          
        'Cursos':Cursos,
        'Unidad':Unidad,
        'Leccion':Leccion
    }
    return render (request,'html/temario.html',context)

def Unidad(request):
    Cursos=curso.objects.all()
    context = {
        'titulo_pagina': 'Nueva Unidad',          
        'Cursos':Cursos,
    }
    return render (request,'html/NewUnidad.html',context)