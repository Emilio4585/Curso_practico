from django.db import models


# Create your models here.
class Conductor(models.Model):
    nombre = models.CharField(default=None, blank=True, max_length=50, null=True)
    telefono = models.CharField(default=None, blank=True, max_length=50, null=True)
    direccion = models.TextField(default=None, blank=True, max_length=50, null=True)
    correo = models.EmailField(default=None, blank=True, max_length=50, null=True)
    imagen = models.ImageField(max_length=100, null=True, upload_to='projects/renta_coches/conductores/',
                               verbose_name='Imagen',
                               blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'
