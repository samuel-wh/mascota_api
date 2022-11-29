from django.db import models
from apps.persona.models import Persona


# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Vacuna')

    def __str__(self):
        return self.nombre


# Modelo Mascota para la base de datos
MACHO = 0
HEMBRA = 1
SEXO = ((MACHO, 'Macho'), (HEMBRA, 'Hembra'))


class Mascota(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    sexo = models.PositiveSmallIntegerField(verbose_name='Sexo', choices=SEXO)
    edad = models.PositiveSmallIntegerField(verbose_name='Edad')
    fecha_rescate = models.DateField(verbose_name='Fecha de rescate')
    foto = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name='Foto')
    # Relaciones
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna)

