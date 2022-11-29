# DJANGO
from django.urls import reverse

# APIs
from apps.mascota.api.views.ApiViews import ApiViewMascota, ApiViewDetalleMascota

# UTILS
from apps.mascota.utils import Pet

# Create your views here.
pet = Pet(decorador_api_view=False, viewset=False)


def crear_mascota(request):
    url_cancelar = reverse('apiview-mascota-lista')
    return pet.crear(request, ApiViewMascota, url_cancelar)


def mascota_lista(request):
    return pet.listar(request, ApiViewMascota)


def mascota_eliminar(request, pk):
    url_cancelar = reverse('apiview-mascota-lista')
    return pet.eliminar(request, ApiViewDetalleMascota, url_cancelar, pk)


def mascota_actualizar(request, pk):
    url_cancelar = reverse('apiview-mascota-lista')
    return pet.actualizar(request, ApiViewDetalleMascota, url_cancelar, pk)
