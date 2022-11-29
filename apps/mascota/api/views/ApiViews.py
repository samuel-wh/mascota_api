# REST FRAMEWORK
from datetime import datetime, date

from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

# SERIALIZERS
from ..serializers import PetSerializer


# API VIEW
class ApiViewMascota(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    @staticmethod
    def get(request):
        pet = PetSerializer.Meta.model.objects.all()
        pet_json = PetSerializer(pet, many=True)
        return Response(pet_json.data)

    @staticmethod
    def post(request):
        data = request.data.copy()
        fecha = data.get('fecha_rescate')
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        fecha = date.strftime(fecha, '%Y-%m-%d')
        data['fecha_rescate'] = fecha
        pet_json = PetSerializer(data=data)
        if pet_json.is_valid():
            pet_json.save()
            return Response(pet_json.data, status=status.HTTP_201_CREATED)
        return Response(pet_json.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiViewDetalleMascota(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    @staticmethod
    def __get_object(pk):
        try:
            return PetSerializer.Meta.model.objects.get(pk=pk)
        except PetSerializer.Meta.model.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        pet = self.__get_object(pk)
        pet_json = PetSerializer(pet)
        return Response(pet_json.data)

    def put(self, request, pk):
        pet = self.__get_object(pk)
        data = request.data.copy()
        fecha = data.get('fecha_rescate')
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        fecha = date.strftime(fecha, '%Y-%m-%d')
        data['fecha_rescate'] = fecha
        pet_json = PetSerializer(pet, data=data)
        if pet_json.is_valid():
            pet_json.save()
            return Response(pet_json.data)
        return Response(pet_json.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pet = self.__get_object(pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApiViewDetallePersonaMascota(APIView):
    @staticmethod
    def __get_object(pk):
        try:
            return PetSerializer.Meta.model.objects.get(pk=pk)
        except PetSerializer.Meta.model.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        pet = self.__get_object(pk)
        pet_json = PetSerializer(pet)
        return Response(pet_json.data.get('persona'))
