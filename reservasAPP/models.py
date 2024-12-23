from django.db import models

# Create your models here.
class Reserva(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    fecha_reserva = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.CharField(max_length=20)
    observacion = models.TextField(blank=True)
    
    def __str__(self):
        return f'Reserva {self.nombre} - {self.fecha_reserva} - {self.hora}'
    