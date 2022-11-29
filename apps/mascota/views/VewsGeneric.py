# DJANGO
from django.urls import reverse

# APIs
from apps.mascota.api.views.GenericViews import GenericMascotaView, GenericDetalleMascota

# UTILS
from ..utils import Pet

pet = Pet(decorador_api_view=False, viewset=False)


# Create your views here.
def crear_mascota(request):
    url_cancelar = reverse('genericview-mascota-lista')
    return pet.crear(request, GenericMascotaView, url_cancelar)


def mascota_lista(request):
    return pet.listar(request, GenericMascotaView)


def mascota_eliminar(request, pk):
    url_cancelar = reverse('genericview-mascota-lista')
    return pet.eliminar(request, GenericDetalleMascota, url_cancelar, pk)


def mascota_actualizar(request, pk):
    url_cancelar = reverse('genericview-mascota-lista')
    return pet.actualizar(request, GenericDetalleMascota, url_cancelar, pk)
