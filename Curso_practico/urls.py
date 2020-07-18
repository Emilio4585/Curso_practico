"""Curso_practico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import settings  # add this for media
from django.contrib.staticfiles.urls import static  # add this for media
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # add this for media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.web_personal.web_personal.urls'), name='web_personal'),
    # renta de coches
    path('renta/', include('apps.proyectos.renta_coches.coches.urls'), name='coches'),
    path('renta/', include('apps.proyectos.renta_coches.conductores.urls'), name='conductores'),
    path('renta/', include('apps.proyectos.renta_coches.pasajero.urls'), name='pasajeros'),
    path('renta/', include('apps.proyectos.renta_coches.reserva.urls'), name='reservas'),
    path('renta/', include('apps.proyectos.renta_coches.rutas.urls'), name='rutas'),
    # path('farmacia/', include('apps.proyectos.farmacia.urls'), name='farmacia'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # add this for media
