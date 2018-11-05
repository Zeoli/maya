from django import forms
from .models import curso,unidad,leccion

class PostForm(forms.ModelForm):

    class Meta:
        model = curso
        fields = ('idCurso','nombre', 'descripcion','fechaFinalCurso')

class UnidadForm(forms.ModelForm):

    class Meta:
        model = unidad
        fields = ('idCurso','nombre')
    
class LeccionForm(forms.ModelForm):

    class Meta:
        model = leccion
        fields = ('idUnidad','nombre',"tema")

        
        