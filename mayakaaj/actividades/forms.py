from django import forms
from .models import pregunta,respuesta,actividad,diccionario,Multimedia

"""
#Formulario de Pregunta
class Pregunta(forms.ModelForm):
    class Meta:
        model = pregunta
        fields = ('idPregunta','tipo', 'pregunta','valor')

#Formulario de respuesta
class Respuesta(forms.ModelForm):
    class Meta:
        model = respuesta
        fields = ('idPregunta','tipo', 'pregunta','valor')
"""
#Formulario de Actividad
class Actividad(forms.ModelForm):
    class Meta:
        model = actividad
        fields = ('idLeccion','habilidad', 'tipo','porcentaje')
 
class DiccionarioForm(forms.ModelForm):

    class Meta:
        model = diccionario
        fields = ('idLeccion','palabra','traduccion','imagen')

class multimedia(forms.ModelForm):

    class Meta:
        model = Multimedia
        fields = ('tipo','archivo')
