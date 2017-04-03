from django.contrib import admin

# Register your models here.
from aplicacion.models import Materia, Estudiante

admin.site.register(Materia)
admin.site.register(Estudiante)