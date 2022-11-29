from rest_framework.routers import DefaultRouter
from apps.mascota.api.views.ViewSet import ViewSetMascota
router = DefaultRouter()
router.register(r'viewset/mascota', ViewSetMascota)
urlpatterns = router.urls
