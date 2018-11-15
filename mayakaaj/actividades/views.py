from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader, RequestContext

from .models import pregunta,respuesta,actividad,diccionario,examen
from .forms import Actividad,DiccionarioForm,multimedia

#View 
def view(request):
    context = {
        'titulo_pagina': 'Contenido'        
    }
    return render (request,'html/contenido.html',context)

#
def listaActividades(request):
    Actividad = actividad.objects.all()
    context = {
        'titulo_pagina': 'Actividades',
        'Actividad':Actividad    
    }
    return render (request,'html/actividades.html',context)
#
def examenes(request):
    Examen = examen.objects.all()
    context = {
        'titulo_pagina': 'Examenes',
        'Examen':Examen    
    }
    return render (request,'html/examenes.html',context)

def palabras(request):
    Palabra = diccionario.objects.all()
    context = {
        'titulo_pagina': 'Palabras Claves',
        'Palabra':Palabra    
    }
    return render (request,'html/diccionario.html',context)
#------------------------------------- Formularios
#Formulario para diccionario
def FormDiccionario(request):
    if request.method == 'POST':
        form = DiccionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect('palabras')    
    else:
        form = DiccionarioForm()
        context = {
            'titulo_pagina': 'Diccionario',                    
            'form': form
        }
        return render(request,'html/AddDiccionario.html', context)
        #return render('html/AddDiccionario.html', locals(), context_instance=RequestContext(request))


#Form Actividades
def actividades(request):
    if request.method == 'POST':
        form = Actividad(request.POST)
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect('listaActividades')   #Redireccionando a temario
    else:
        form = Actividad() #Llamando al formulario de curso
        context = {
            'titulo_pagina': 'Nueva Actividad',          
            'form': form
        }
        return render(request, 'html/NewActividad.html', context)

#Multimedia
def formMultimedia(request):
    if request.method == 'POST':
        form = multimedia(request.POST,request.FILES)
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect('listaActividades')   #Redireccionando a temario
    else:
        form = multimedia() #Llamando al formulario de curso
        context = {
            'titulo_pagina': 'Agregando Multimedia',          
            'form': form
        }
        return render(request, 'html/AddMultimedia.html', context)