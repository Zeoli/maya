from djongo import models
from cursos.models import models
from datetime import datetime 

#-----------------Actividades:

class tipoActividad (models.Model):
    idTipoAct = models.AutoField(primary_key=True)
    tipo= models.CharField(max_length=50,verbose_name="Tipo")
    class Meta:
        verbose_name_plural = "Tipos Actividades"

    def __str__(self):
        return self.tipo

class habilidad (models.Model):
    idHabilidad = models.AutoField(primary_key=True)
    habilidad= models.CharField(max_length=50,verbose_name="Tipo")
    class Meta:
        verbose_name_plural = "habilidades"

    def __str__(self):
        return self.habilidad

class actividad(models.Model):
    idActividad = models.AutoField(primary_key=True)
    idLeccion =  models.ForeignKey('cursos.leccion', on_delete=models.CASCADE,verbose_name="Leccion")
    habilidad = models.ForeignKey('habilidad', on_delete=models.CASCADE,verbose_name="Habilidad")
    tipo = models.ForeignKey('tipoActividad', on_delete=models.CASCADE,verbose_name="Tipo")
    porcentaje=models.CharField(max_length=50,verbose_name="Porcentaje")
    titulo = models.CharField(max_length=50,verbose_name="Titulo")
    instrucciones= models.CharField(max_length=10,verbose_name="Instrucciones")
    class Meta:
        #abstract = True
        verbose_name_plural = "actividades"

    def __str__(self):
        return self.titulo

#---------------Preguntas:
class tipoPregunta (models.Model):
    idTipoPreg = models.AutoField(primary_key=True)
    tipo= models.CharField(max_length=50,verbose_name="Tipo")
    class Meta:
        verbose_name_plural = "Tipo de Preguntas"

    def __str__(self):
        return self.tipo


class respuesta(models.Model):
    Respuesta = models.CharField(max_length=50)
    class Meta:
        abstract = True
    def __str__(self):
        return self.Respuesta


class pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True)
    tipo = tipo = models.ForeignKey('tipoPregunta', on_delete=models.CASCADE,verbose_name="Tipo")
    pregunta =  models.CharField(max_length=50,verbose_name="Pregunta")
    valor=models.CharField(max_length=50,verbose_name="Valor")
    respuesta = models.EmbeddedModelField(
        model_container=respuesta
    )
    #id
    class Meta:           
        verbose_name_plural = "preguntas"

    def __str__(self):
        return self.pregunta


#-----------------------Diccionario:
class diccionario(models.Model):
    idDiccionario = models.AutoField(primary_key=True)
    idLeccion =  models.ForeignKey('cursos.leccion', on_delete=models.CASCADE,verbose_name="Leccion")
    palabra = models.CharField(max_length=50,verbose_name="Palabra")
    traduccion = models.CharField(max_length=50,verbose_name="Traduccion")
    imagen=models.ImageField(verbose_name="Imagen",upload_to="projects")
    class Meta:
        verbose_name_plural = "diccionarios"

    def __str__(self):
        return self.palabra

#----------------------- Multimedia:
class Multimedia (models.Model):
    idMultimedia= models.AutoField(primary_key=True)
    tipo= models.CharField(max_length=50,verbose_name="Nombre")
    archivo = models.FileField(upload_to="files/%Y/%m/%d/",verbose_name="Archivo")
    class Meta:
        verbose_name_plural = "Multimedias"

    def __str__(self):
        return self.nombre
#------------------------- Examenes:

class examen(models.Model):
    idExamen = models.AutoField(primary_key=True)
    idUnidad =  models.ForeignKey('cursos.unidad', on_delete=models.CASCADE,verbose_name="Unidad")
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    calificacion = models.IntegerField (verbose_name="Calificacion")
    fecha = models.DateTimeField(default=datetime.now, verbose_name="Fecha dde examen")
    preguntas = models.ManyToManyField(pregunta)
    class Meta:
        verbose_name_plural = "examenes"

    def __str__(self):
        return self.nombre

class resultados(models.Model):
    idResultado = models.AutoField(primary_key=True)
    idExamen =  models.ForeignKey('examen', on_delete=models.CASCADE,verbose_name="examen")
    calificacion = models.FloatField(max_length=50,verbose_name="calificacion")
    class Meta:
        verbose_name_plural = "resultados"

    def __str__(self):
        return self.idResultado