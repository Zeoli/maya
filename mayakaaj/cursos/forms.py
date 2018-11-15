from django import forms
from .models import curso,unidad,leccion

#Form Curso
class PostForm(forms.ModelForm):

    class Meta:
        model = curso
        fields = ('idCurso','nombre', 'descripcion','fechaFinalCurso')

#Form Unidad
class UnidadForm(forms.ModelForm):

    class Meta:
        model = unidad
        fields = ('idCurso','nombre')

#Form Leccion
class LeccionForm(forms.ModelForm):

    class Meta:
        model = leccion
        fields = ('idUnidad','nombre','tema')  
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
        }
        