from django import forms
from ..models import Mascota, Vacuna


class PetForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = ('nombre', 'sexo', 'edad', 'fecha_rescate', 'foto', 'persona', 'vacuna')

