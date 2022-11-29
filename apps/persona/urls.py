from django.urls import path
from .views import crear_persona


urlpatterns = [
    # URLS CLASS VIEW
    path('persona-nuevo', crear_persona, name='persona-nuevo'),
]
