#forms.py
from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    
    class Meta:
        ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

        model = Reserva
        fields = ['nombre', 'telefono', 'fecha_reserva', 'hora', 'cantidad_personas', 'estado', 'observacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
            'fecha_reserva': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 15}),
            'estado': forms.Select(attrs={'class': 'form-control'}, choices=ESTADO_CHOICES),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese alguna observación (opcional)'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
