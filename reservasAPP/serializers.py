from rest_framework import serializers
from reservasAPP.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'nombre', 'telefono', 'fecha_reserva', 'hora', 'cantidad_personas', 'estado', 'observacion']