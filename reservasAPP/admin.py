from django.contrib import admin
from reservasAPP.models import Reserva
# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'fecha_reserva', 'hora', 'cantidad_personas', 'estado', 'observacion')

admin.site.register(Reserva, ReservaAdmin)
