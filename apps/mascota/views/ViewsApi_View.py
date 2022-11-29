# DJANGO
from django.urls import reverse

# APIs
from ..api.views.api_view import api_view_mascota, api_view_detalle_mascota

# UTILS
from apps.mascota.utils import Pet

# Create your views here.
pet = Pet(decorador_api_view=True, viewset=False)


def crear_mascota(request):
    url_cancelar = reverse('@api_view-mascota-lista')
    return pet.crear(request, api_view_mascota, url_cancelar)


def mascota_lista(request):
    return pet.listar(request, api_view_mascota)


def mascota_eliminar(request, pk):
    url_cancelar = reverse('@api_view-mascota-lista')
    return pet.eliminar(request, api_view_detalle_mascota, url_cancelar, pk)


def mascota_actualizar(request, pk):
    url_cancelar = reverse('@api_view-mascota-lista')
    return pet.actualizar(request, api_view_detalle_mascota, url_cancelar, pk)
