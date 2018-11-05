from django.urls import path
from . import views

urlpatterns = [
    path('temario', views.temario, name='temario'),
    path('unidad', views.Unidad, name='unidad'),
    path('leccion', views.Leccion, name='leccion'),
    path('lecciones', views.ViewLeccion, name='lecciones'),
    path('formulario', views.formulario, name='formulario'),
]