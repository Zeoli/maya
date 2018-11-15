from django.urls import path
from . import views

urlpatterns = [
    path('addActividades', views.actividades, name='addActividades'),
    path('diccionario', views.FormDiccionario, name='diccionario'),
    path('palabras', views.palabras, name='palabras'),
    path('contenido', views.view, name='contenido'),
    path('actividades', views.listaActividades, name='actividades'),
    path('examenes', views.examenes, name='examenes'),
    path('addMultimedia', views.formMultimedia, name='addMultimedia'),
]