from django.contrib import admin

from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'dueno', 'especie', 'fecha_registro')
    search_fields = ('mascota', 'dueno')
