from django.db import models
from django.utils import timezone
# Create your models here.
from apps.proyectos.renta_coches.conductores.models import Conductor
from apps.proyectos.renta_coches.pasajero.models import Pasajero


class Reserva(models.Model):
    titulo = models.CharField(default=None, blank=True, max_length=50, null=True)
    descripcion = models.TextField(default=None, blank=True, max_length=50, null=True)
    tipo = models.CharField(default=None, blank=True, max_length=50, null=True)
    boleto = models.CharField(default=None, blank=True, max_length=50, null=True)
    fecha = models.DateField(auto_now_add=True)
    pasajero = models.OneToOneField(
        Pasajero,
        on_delete=models.CASCADE,
        null=True
    )
    conductor = models.OneToOneField(
        Conductor,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
