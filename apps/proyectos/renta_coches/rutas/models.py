from django.db import models


# Create your models here.
class Ruta(models.Model):
    nombre = models.CharField(default=None, blank=True, max_length=50, null=True)
    tipo = models.CharField(default=None, blank=True, max_length=50, null=True)
    descripcion = models.TextField(default=None, blank=True, max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
