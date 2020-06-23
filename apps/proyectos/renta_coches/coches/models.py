from django.db import models


# Create your models here.
class Coches(models.Model):
    # id_propietario = models.IntegerField(default=None, blank=True,null=True)
    numero = models.CharField(default=None, blank=True, max_length=50, null=True)
    tipo = models.CharField(default=None, blank=True, max_length=50, null=True)
    categoria = models.CharField(default=None, blank=True, max_length=50, null=True)
    nombre = models.CharField(default=None, blank=True, max_length=50, null=True)
    nombre = models.ImageField(default=None, blank=True, max_length=50, null=True)
    imagen = models.ImageField(max_length=100, null=True, upload_to='projects/renta_coches/coches/',
                               verbose_name='Imagen',
                               blank=True)

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'Coche'
        verbose_name_plural = 'Coches'
