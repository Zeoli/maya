from django.db import models
from datetime import datetime  
# Create your models here.
class grupo(models.Model):
    idGrupo = models.AutoField(primary_key=True)
    idCurso = models.ForeignKey('cursos.curso', on_delete=models.CASCADE ,verbose_name="Curso")
    idDocente = models.ForeignKey('docente.docente', on_delete=models.CASCADE ,verbose_name="Docente")
    nombre = models.CharField(max_length=50,verbose_name="Nombre")    
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    def __str__(self):
        return self.nombre

