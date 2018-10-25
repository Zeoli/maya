from django.urls import path
from . import views

urlpatterns = [
    path('temario', views.temario, name='temario'),
    path('unidad', views.Unidad, name='unidad'),
]