from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ruta

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms


class RutaListado(ListView):
    model = Ruta


class RutaDetalle(DetailView):
    model = Ruta


class RutaCrear(SuccessMessageMixin, CreateView):
    model = Ruta
    form = Ruta
    fields = "__all__"
    success_message = 'Ruta Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Ruta

    # Redireccionamos a la página principal luego de crear un registro o ruta
    def get_success_url(self):
        return reverse('leer_ruta')  # Redireccionamos a la vista principal 'leer'


class RutaActualizar(SuccessMessageMixin, UpdateView):
    model = Ruta
    form = Ruta
    fields = "__all__"
    success_message = 'Ruta Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Ruta

    # Redireccionamos a la página principal luego de actualizar un registro o ruta
    def get_success_url(self):
        return reverse('leer_ruta')  # Redireccionamos a la vista principal 'leer'


class RutaEliminar(SuccessMessageMixin, DeleteView):
    model = Ruta
    form = Ruta
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o ruta
    def get_success_url(self):
        success_message = 'Ruta Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Ruta
        messages.success(self.request, (success_message))
        return reverse('leer_ruta')  # Redireccionamos a la vista principal 'leer'
