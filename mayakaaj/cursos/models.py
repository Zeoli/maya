from djongo import models
from datetime import datetime  
from ckeditor.fields import RichTextField
# Create your models here.
class curso(models.Model):
    idCurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    descripcion=models.TextField(verbose_name="Descripcion")
    fechaInicioCurso = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Inicio")
    fechaFinalCurso = models.DateTimeField(default=datetime.now, verbose_name="Fecha de Fin")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")
    
    def __str__(self):
        return self.nombre

class leccion(models.Model):
    idLeccion = models.AutoField(primary_key=True)
    idUnidad =  models.ForeignKey('unidad', on_delete=models.CASCADE,verbose_name="Unidad")
    nombre = models.CharField(max_length=50,verbose_name = " Nombre " )
    tema = RichTextField()
    
    class Meta:
        #abstract = True
        verbose_name_plural = "lecciones"

    def __str__(self):
        return self.nombre
 

class unidad(models.Model):
    idUnidad = models.AutoField(primary_key=True)
    idCurso = models.ForeignKey('curso', on_delete=models.CASCADE ,verbose_name="Curso")
    nombre = models.CharField(max_length=50,verbose_name="Nombre")

    class Meta:
        #abstract=True
        verbose_name_plural = "unidades"

    def __str__(self):
        return self.nombre

