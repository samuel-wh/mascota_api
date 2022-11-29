from django.urls import path
from .views.GenericViews import GenericMascotaView, GenericDetalleMascota, GenericDetallePersonaMascota
from .views.ApiViews import ApiViewMascota, ApiViewDetalleMascota, ApiViewDetallePersonaMascota
from .views.api_view import api_view_mascota, api_view_detalle_mascota, api_view_detalle_mascota_persona

urlpatterns = [
    # GENERIC
    path('generic/mascota/', GenericMascotaView.as_view()),
    path('generic/mascota/<int:pk>', GenericDetalleMascota.as_view()),
    path('generic/mascota/<int:pk>/persona', GenericDetallePersonaMascota.as_view()),

    # APIVIEW
    path('apiview/mascota/', ApiViewMascota.as_view()),
    path('apiview/mascota/<int:pk>', ApiViewDetalleMascota.as_view()),
    path('apiview/mascota/<int:pk>/persona', ApiViewDetallePersonaMascota.as_view()),

    # VIEWSET
    # Utiliza el archivo routers.py

    # @api_view
    path('decorador/mascota/', api_view_mascota),
    path('decorador/mascota/<int:pk>', api_view_detalle_mascota),
    path('decorador/mascota/<int:pk>/persona', api_view_detalle_mascota_persona),

]
