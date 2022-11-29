from datetime import datetime, date

from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import PetSerializer


# VIEWSET
class ViewSetMascota(viewsets.ModelViewSet):
    queryset = PetSerializer.Meta.model.objects.all()
    serializer_class = PetSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        fecha = data.get('fecha_rescate')
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        fecha = date.strftime(fecha, '%Y-%m-%d')
        data['fecha_rescate'] = fecha
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        fecha = data.get('fecha_rescate')
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        fecha = date.strftime(fecha, '%Y-%m-%d')
        data['fecha_rescate'] = fecha
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def persona(self, request, pk):
        try:
            mascota = PetSerializer.Meta.model.objects.get(pk=pk)
        except PetSerializer.Meta.model.DoesNotExist as e:
            raise Http404
        pet_json = PetSerializer(mascota)
        return Response(pet_json.data.get('persona'))
