from django.contrib import admin

from .models import Grupo, Curso, Alumno, AulaVirtual

admin.site.register(Grupo)
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(AulaVirtual)

# Register your models here.
