from django.contrib import admin
from .models import curso,unidad,leccion

#from .embedded_models import unidad,leccion

#admin.site.register([unidad,leccion])

admin.site.register(curso)
admin.site.register(unidad)
admin.site.register(leccion)