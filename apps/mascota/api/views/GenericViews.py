# REST FRAMEWORK
from rest_framework import mixins, generics, status
from rest_framework.response import Response

# SERIALIZERS
from ..serializers import PetSerializer
from datetime import datetime, date

# GENERIC API VIEW
class GenericMascotaView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = PetSerializer.Meta.model.objects.all()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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


class GenericDetalleMascota(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                            generics.GenericAPIView):
    queryset = PetSerializer.Meta.model.objects.all()
    serializer_class = PetSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        fecha = data.get('fecha_rescate')
        fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y')
        fecha = datetime.date.strftime(fecha, '%Y-%m-%d')
        data['fecha_rescate'] = fecha
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GenericDetallePersonaMascota(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = PetSerializer.Meta.model.objects.all()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        pet_json = self.retrieve(request, *args, **kwargs)
        return Response(pet_json.data.get('persona'))

