from rest_framework import serializers
from ..models import Persona, Solicitud


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'apellidos', 'edad', 'telefono', 'email', 'domicilio')


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id', 'numero_mascotas', 'razones', 'persona')

    def to_representation(self, instance):
        self.fields['persona'] = PersonaSerializer(read_only=True)
        return super(SolicitudSerializer, self).to_representation(instance)

