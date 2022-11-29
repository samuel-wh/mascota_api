# DJANGO
from django.urls import reverse

# APIs
from apps.mascota.api.views.ViewSet import ViewSetMascota

# UTILs
from ..utils import Pet

# Create your views here.
pet = Pet(decorador_api_view=False, viewset=True)


def crear_mascota(request):
    url_cancelar = reverse('viewset-mascota-lista')
    return pet.crear(request, ViewSetMascota, url_cancelar)


def mascota_lista(request):
    return pet.listar(request, ViewSetMascota)


def mascota_eliminar(request, pk):
    is_viewset = True
    url_cancelar = reverse('viewset-mascota-lista')
    return pet.eliminar(request, ViewSetMascota, url_cancelar, pk)


def mascota_actualizar(request, pk):
    is_viewset = True
    url_cancelar = reverse('viewset-mascota-lista')
    return pet.actualizar(request, ViewSetMascota, url_cancelar, pk)
