from django.urls import path
from . import views

urlpatterns = [
    path('temario', views.temario, name='temario'),
]