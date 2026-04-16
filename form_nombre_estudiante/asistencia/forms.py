from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre completo'}),
            'documento_identidad': forms.TextInput(attrs={'placeholder': 'Ingrese el documento'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'fecha_asistencia': forms.DateInput(attrs={'type': 'date'}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
            'observaciones': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Observaciones opcionales'
            }),
        }