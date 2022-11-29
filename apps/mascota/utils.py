from datetime import datetime, date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status

from apps.mascota.forms.mascota_forms import PetForm


class Pet:

    def __init__(self, decorador_api_view, viewset):
        self.__decorador_api_view = decorador_api_view
        self.__viewset = viewset

    def crear(self, request, apiview, url_cancelar):

        if request.method == 'POST':
            form = PetForm(request.POST, request.FILES)
            if form.is_valid():
                if self.__viewset:
                    instance_api_pet = apiview.as_view({'post': 'create'})(request=request)
                elif self.__decorador_api_view:
                    instance_api_pet = apiview(request=request)
                else:
                    instance_api_pet = apiview.as_view()(request=request)
                print(instance_api_pet.status_code)
                if instance_api_pet.status_code == status.HTTP_201_CREATED:
                    print("Se registro")
                    return HttpResponseRedirect(url_cancelar)
                else:
                    print("No se registro")
                    print(instance_api_pet.data)
            else:
                print("Form no es valido")
        else:
            form = PetForm()
        return render(request, 'mascota_agregar.html', {'form': form, 'url_cancelar': url_cancelar})

    def listar(self, request, apiview):
        mascota = None
        if request.method == 'GET':
            if self.__viewset:
                instance_api_pet = apiview.as_view({'get': 'list'})(request=request)
            elif self.__decorador_api_view:
                instance_api_pet = apiview(request=request)
            else:
                instance_api_pet = apiview.as_view()(request=request)
            if instance_api_pet.status_code == status.HTTP_200_OK:
                mascota = instance_api_pet.data
                for i in mascota:
                    fecha = i.get('fecha_rescate')
                    fecha = datetime.strptime(fecha, '%Y-%m-%d')
                    fecha = date.strftime(fecha, '%d-%m-%Y')
                    i['fecha_rescate'] = fecha
        return render(request, 'mascota_lista.html', {'mascota': mascota})

    def eliminar(self, request, apiview, url_cancelar, pk):
        mascota = None
        if self.__viewset:
            instance_api_mascota = apiview.as_view({'get': 'retrieve'})(request=request, pk=pk)
        elif self.__decorador_api_view:
            instance_api_mascota = apiview(request=request, pk=pk)
        else:
            instance_api_mascota = apiview.as_view()(request=request, pk=pk)
        if instance_api_mascota.status_code == status.HTTP_200_OK:
            mascota = instance_api_mascota.data
        if request.method == 'POST':
            request.method = 'DELETE'
            if self.__viewset:
                instace_api_mascota = apiview.as_view({'delete': 'destroy'})(request=request, pk=pk)
            elif self.__decorador_api_view:
                instace_api_mascota = apiview(request=request, pk=pk)
            else:
                instace_api_mascota = apiview.as_view()(request=request, pk=pk)
            if instace_api_mascota == status.HTTP_204_NO_CONTENT:
                print("Se elimino")
                return HttpResponseRedirect(url_cancelar)
            else:
                print("No se elimino")
                return HttpResponseRedirect(url_cancelar)
        return render(request, 'mascota_eliminar.html', {'mascota': mascota, 'url_cancelar': url_cancelar})

    def actualizar(self, request, apiview, url_cancelar, pk):
        form = None
        if request.method == 'GET':
            if self.__viewset:
                mascota = apiview.as_view({'get': 'retrieve'})(request=request, pk=pk)
            elif self.__decorador_api_view:
                mascota = apiview(request=request, pk=pk)
            else:
                mascota = apiview.as_view()(request=request, pk=pk)
            if mascota.status_code == status.HTTP_404_NOT_FOUND:
                print("no existe la mascota")
            else:
                mascota = mascota.data.serializer.instance
                form = PetForm(instance=mascota)
        else:
            request.method = 'GET'
            if self.__viewset:
                mascota = apiview.as_view({'get': 'retrieve'})(request=request, pk=pk)
            elif self.__decorador_api_view:
                mascota = apiview(request=request, pk=pk)
            else:
                mascota = apiview.as_view()(request=request, pk=pk)
            mascota = mascota.data.serializer.instance
            form = PetForm(request.POST, request.FILES, instance=mascota)
            if form.is_valid():
                request.method = 'PUT'
                if self.__viewset:
                    instance_api_pet = apiview.as_view({'put': 'update'})(request=request, pk=pk)
                elif self.__decorador_api_view:
                    instance_api_pet = apiview(request=request, pk=pk)
                else:
                    instance_api_pet = apiview.as_view()(request=request, pk=pk)
                print(instance_api_pet.status_code)
                if instance_api_pet.status_code == status.HTTP_200_OK:
                    print("Se Actualizo")
                    return HttpResponseRedirect(url_cancelar)
                else:
                    print("No se Actualizo")
                    print(instance_api_pet.data)
        return render(request, 'mascota_agregar.html', {'form': form, 'url_cancelar': url_cancelar})
