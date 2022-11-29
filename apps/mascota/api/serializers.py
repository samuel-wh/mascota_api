from rest_framework import serializers
from ..models import Mascota, Vacuna
from ...persona.api.serializers import PersonaSerializer


class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ('id', 'nombre')


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ('id', 'nombre', 'sexo', 'edad', 'fecha_rescate', 'foto', 'persona', 'vacuna')

    def to_representation(self, instance):
        self.fields['vacuna'] = VacunaSerializer(read_only=True, many=True)
        self.fields['persona'] = PersonaSerializer(read_only=True)
        self.fields['foto'] = serializers.ImageField(required=False, max_length=None, allow_null=False,
                                                     allow_empty_file=False, use_url=True)
        return super(PetSerializer, self).to_representation(instance)
