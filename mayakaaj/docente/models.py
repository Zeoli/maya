from django.db import models

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, blank=True)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)

    def __str__(self):
        return self.primer_nombre + ' ' + self.apellido_paterno

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_curso

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=30)
    miembros = models.ManyToManyField(
        'Alumno',
        through = 'AulaVirtual',
        through_fields = ('id_grupo', 'id_alumno'),
    )

    def __str__(self):
        return self.nombre_grupo

class AulaVirtual(models.Model):
    id_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    id_grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)


# Create your models here.
