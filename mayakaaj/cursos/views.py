from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader, RequestContext

from .models import curso,unidad,leccion
from .forms import PostForm,UnidadForm,LeccionForm

#Vista de Temario
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
 #Vista de Leccion
def ViewLeccion(request):
    Cursos=curso.objects.all()
    Unidad = unidad.objects.all()
    Leccion = leccion.objects.all()
    context = {
        'titulo_pagina': 'Lecciones',          
        'Cursos':Cursos,
        'Unidad':Unidad,
        'Leccion':Leccion
    }
    return render (request,'html/lecciones.html',context)
#Formulario Nueva Unidad
def Unidad(request):
    if request.method == 'POST':
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect('temario')    
    else:
        form = UnidadForm()
        context = {
            'titulo_pagina': 'Nueva Unidad',                    
            'form': form
        }
        return render(request, 'html/NewUnidad.html', context)
#Formulario Nueva Leccion
def Leccion(request):
    if request.method == 'POST':
        form = LeccionForm(request.POST)
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect('temario')    
    else:
        form = LeccionForm()
        context = {
            'titulo_pagina': 'Nueva Leccion',                    
            'form': form
        }
        return render(request, 'html/NewLeccion.html', context)

#Formulario de Nuevo Curso
def formulario(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect('temario')    #Redireccionando a temario
    else:
        form = PostForm() #Llamando al formulario de curso
        context = {
            'titulo_pagina': 'Nuevo curso',          
            'form': form
        }
        return render(request, 'html/NewCurso.html', context)
