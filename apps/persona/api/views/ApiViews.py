# REST FRAMEWORK
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
# MODELS
from ...models import Solicitud, Persona

# SERIALIZERS
from ..serializers import SolicitudSerializer, PersonaSerializer


# API VIEW
class ApiViewPersona(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        persona = Persona.objects.all()
        persona_json = SolicitudSerializer(persona, many=True)
        return Response(persona_json.data)

    def post(self, request):

        persona_json = PersonaSerializer(data=request.data)
        if persona_json.is_valid():
            persona_json.save()
            return Response(persona_json.data, status=status.HTTP_201_CREATED)
        return Response(persona_json.errors, status=status.HTTP_400_BAD_REQUEST)

