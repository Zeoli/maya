from django import forms

from .models import unidad,leccion

class Unidad(ModelForm):
    class Meta:
        model = unidad
        