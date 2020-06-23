from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Pasajero(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    telefono = models.CharField(default=None, blank=True, max_length=50, null=True)
    direccion = models.TextField(default=None, blank=True, max_length=50, null=True)
    imagen = models.ImageField(max_length=100, null=True, upload_to='projects/renta_coches/pasajeros',
                               verbose_name='Imagen',
                               blank=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Pasajero'
        verbose_name_plural = 'Pasajeros'
