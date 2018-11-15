from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic.list import ListView
from .models import curso,unidad,leccion
from actividades.models import diccionario
from .forms import PostForm,UnidadForm,LeccionForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

#--------------------------------------------- Listas
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


#Lista de Unidades
class UnidadListView(ListView):
    model = unidad    
    context = {'titulo_pagina':'Unidad'}

#Lista de Lecciones 
def detalleUnidad(request, idUnidad):
    Unidad = unidad.objects.get(pk=idUnidad)
    Leccion = leccion.objects.all()
    context = {
        'titulo_pagina': 'Lecciones', 
        'Unidad': Unidad,
        'Leccion':Leccion
    }
    return render (request,'cursos/leccion_list.html',context)
##
def detalleLeccion(request,idLeccion):
    Leccion = leccion.objects.get(pk=idLeccion)
    Diccionario = diccionario.objects.all()
    print(Leccion)
    print(Diccionario)
    context = {
        'titulo_pagina': 'Lecciones', 
        'Diccionario': Diccionario,
        'Leccion':Leccion
    }
    return render (request,'cursos/leccion_detail.html',context)

###
#class DetailViewLeccion(DetailView):
 #   model = leccion
    

class deleteUnidad ( DeleteView ):
    model = unidad
    success_url = reverse_lazy ( 'unidades' )

class deleteLeccion ( DeleteView ):
    model = leccion
    success_url = reverse_lazy ( 'temario' )

"""
def deleteUnidad(request, idUnidad):
    unidad = unidad.objects.get(id=idUnidad)
    print("x=",unidad)
    print("Y=",idUnidad)

    if request.method == 'POST':
        unidad.delete()
        return HttpResponseRedirect('temario')   

    return render(request, 'html/borrarLeccion.html', {'unidad': unidad })



#Leccion Detalles
def detalleLeccion(request, idLeccion):
    x = leccion.objects.get(pk=idLeccion)
    print("X=",x)
    todo = leccion.objects.all()
    print("T=",todo)
    context = {
        'titulo_pagina': 'Leccion', 
        #'x': x,
        'todo': todo
    }
    return render (request,'html/leccion.html',context)
"""
"""
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
    return render (request,'html/leccion_list.html',context)

def ViewUnidades(request):   
    Unidad = unidad.objects.all()
    Leccion = leccion.objects.all()
    context = {
        'titulo_pagina': 'Lecciones',          
        'Unidad':Unidad,
        'Leccion':Leccion
    }
    return render (request,'html/unidades.html',context)
    """
#----------------------------------------Formularios
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
def Curso(request):
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

"""def borrarLeccion(request, id):
    Leccion = leccion.objects.get(id = id)
    if request.method == 'POST':
        leccion.delete()
        return redirect('temario')

    return render(request, 'html/borrarLeccion.html', { 'Leccion':Leccion })"""
   
