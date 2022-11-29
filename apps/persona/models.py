from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(regex=r'^\d{8,14}((,\d{8,14})?)*$',
                             message="El formato del teléfono debe ser: '9998888777', "
                                     "sin código de país. De 8-14 dígitos permitidos. "
                                     "Puede agregar más telefonos seperados por coma.")


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellidos = models.CharField(max_length=40, verbose_name='Apellidos')
    edad = models.PositiveSmallIntegerField(verbose_name='Edad')
    telefono = models.CharField(max_length=15, validators=[phone_regex], verbose_name="Teléfono Celular")
    email = models.EmailField(verbose_name='Correo')
    domicilio = models.TextField(verbose_name='Domicilio')

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    numero_mascotas = models.PositiveSmallIntegerField(verbose_name='Numero de mascotas')
    razones = models.TextField(verbose_name='Razones')
