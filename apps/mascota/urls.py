from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import ViewsApiView, VewsGeneric, ViewsViewSet, ViewsApi_View

urlpatterns = [
    # APIVIEW
    path('apiview/', ViewsApiView.mascota_lista, name='apiview-mascota-lista'),
    path('apiview/mascota-nuevo/', ViewsApiView.crear_mascota, name='apiview-mascota-crear'),
    path('apiview/mascota-eliminar/<int:pk>', ViewsApiView.mascota_eliminar, name='apiview-mascota-elimar'),
    path('apiview/mascota-actualizar/<int:pk>', ViewsApiView.mascota_actualizar, name='apiview-mascota-actualizar'),

    # GENERICVIEW
    path('genericview/', VewsGeneric.mascota_lista, name='genericview-mascota-lista'),
    path('genericview/mascota-nuevo/', VewsGeneric.crear_mascota, name='genericview-mascota-crear'),
    path('genericview/mascota-eliminar/<int:pk>', VewsGeneric.mascota_eliminar, name='genericview-mascota-elimar'),
    path('genericview/mascota-actualizar/<int:pk>', VewsGeneric.mascota_actualizar,
         name='genericview-mascota-actualizar'),

    # VIEWSET
    path('viewset/', ViewsViewSet.mascota_lista, name='viewset-mascota-lista'),
    path('viewset/mascota-nuevo/', ViewsViewSet.crear_mascota, name='viewset-mascota-crear'),
    path('viewset/mascota-eliminar/<int:pk>', ViewsViewSet.mascota_eliminar, name='viewset-mascota-elimar'),
    path('viewset/mascota-actualizar/<int:pk>', ViewsViewSet.mascota_actualizar, name='viewset-mascota-actualizar'),

    # @api_view
    path('@api_view/', ViewsApi_View.mascota_lista, name='@api_view-mascota-lista'),
    path('@api_view/mascota-nuevo/', ViewsApi_View.crear_mascota, name='@api_view-mascota-crear'),
    path('@api_view/mascota-eliminar/<int:pk>', ViewsApi_View.mascota_eliminar, name='@api_view-mascota-elimar'),
    path('@api_view/mascota-actualizar/<int:pk>', ViewsApi_View.mascota_actualizar, name='@api_view-mascota-actualizar'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
