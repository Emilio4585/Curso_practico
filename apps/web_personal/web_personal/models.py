from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    career = models.CharField(max_length=50, verbose_name='Carrera')
    year = models.DateField(auto_now_add=True, verbose_name='Año')
    description = models.TextField(max_length=500, verbose_name='Descripcion')
    phone = models.CharField(max_length=50, verbose_name='Telefono')
    fee = models.CharField(max_length=50, verbose_name='Honorarios')
    biography = models.TextField(max_length=500, verbose_name='Biografia')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Projects(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Nombre')
    description = models.TextField(max_length=500, null=True, verbose_name='Descripcion')
    link = models.CharField(max_length=100, null=True, verbose_name='Link')
    image = models.ImageField(max_length=100, null=True, upload_to='web_personal/projects', verbose_name='Imagen',
                              blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateField(auto_now_ad=True, verbose_name='Año')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Skills(models.Model):
    name = models.CharField(max_length=50, null=True)
    domain = models.IntegerField(null=True)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
