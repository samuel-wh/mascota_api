from django import forms
from ..models import Solicitud, Persona


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ('numero_mascotas', 'razones', 'persona')


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellidos', 'edad', 'telefono', 'email', 'domicilio')
