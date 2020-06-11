from django.db import models
from django.contrib.auth.models import User as usr


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(
        usr,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    career = models.CharField(max_length=50)
    year = models.DateField()
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=50)
    fee = models.CharField(max_length=50)
    biography = models.TextField(max_length=500)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=500, null=True)
    link = models.CharField(max_length=100, null=True)
    image = models.ImageField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    domain = models.IntegerField(null=True)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
