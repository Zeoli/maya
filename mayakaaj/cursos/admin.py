from django.contrib import admin
from .models import curso,unidad,leccion

admin.site.register(curso)
admin.site.register(unidad)
admin.site.register(leccion)

class Media:
        css = {
            'all': ('css/custom_ckeditor.css',)
        }