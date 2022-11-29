# REST FRAMEWORK
from datetime import datetime, date

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# SERIALIZERS
from ..serializers import PetSerializer


# @api_view
def get_object(pk):
    try:
        return PetSerializer.Meta.model.objects.get(pk=pk)
    except PetSerializer.Meta.model.DoesNotExist as e:
        raise Http404


@api_view(['GET', 'POST'])
def api_view_mascota(request):
    if request.method == 'GET':
        pet = PetSerializer.Meta.model.objects.all()
        pet_json = PetSerializer(pet, many=True)
        return Response(pet_json.data)

    if request.method == 'POST':
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


@api_view(['GET', 'PUT', 'DELETE'])
def api_view_detalle_mascota(request, pk):

    if request.method == 'GET':
        pet = get_object(pk)
        pet_json = PetSerializer(pet)
        return Response(pet_json.data)

    elif request.method == 'PUT':
        pet = get_object(pk)
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

    elif request.method == 'DELETE':
        pet = get_object(pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def api_view_detalle_mascota_persona(request, pk):

    if request.method == 'GET':
        pet = get_object(pk)
        pet_json = PetSerializer(pet)
        return Response(pet_json.data.get('persona'))
