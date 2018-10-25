from djongo import models

class docente(models.Model):
    idDocente = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=30, verbose_name="Nombre")
    segundo_nombre = models.CharField(max_length=30, blank=True,verbose_name=" " )
    apellido_paterno = models.CharField(max_length=30, verbose_name="Apellido")
    apellido_materno = models.CharField(max_length=30, verbose_name=" ")
    telefono = models.CharField(max_length=10,verbose_name= "Telefono")
    

    def __str__(self):
        return self.primer_nombre + ' ' + self.apellido_paterno
"""
class MaestroGrupo (models.Model):

    idDocente = models.ForeignKey('docente', on_delete=models.CASCADE)
    docente.primer_nombre = models.ForeignKey('docente', on_delete=models.CASCADE)
    docente.apellido_paterno = models.ForeignKey('docente', on_delete=models.CASCADE)
    idGrupo = models.ForeignKey('grupos.grupo', on_delete=models.CASCADE ,verbose_name="Grupo")
    

    def __str__(self):
        return self.docente.primer_nombre


class GrupoDocente(models.Model):
    idGrupoDocente = models.AutoField(primary_key=True)
    nombre = models.ForeignKey('grupos.grupo', on_delete=models.CASCADE ,verbose_name="Grupo")
    miembros = models.ManyToManyField(
        'docente',
        through = 'grupos.grupo',
        through_fields = ('idGrupo', 'idDocente'),
    )

    def __str__(self):
        return self.nombre

class AulaVirtual(models.Model):
    id_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    id_grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)

"""
# Create your models here.
