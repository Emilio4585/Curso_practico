from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pasajero

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms


class PasajeroListado(ListView):
    model = Pasajero


class PasajeroDetalle(DetailView):
    model = Pasajero


class PasajeroCrear(SuccessMessageMixin, CreateView):
    model = Pasajero
    form = Pasajero
    fields = "__all__"
    success_message = 'Pasajero Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Pasajero

    # Redireccionamos a la página principal luego de crear un registro o pasajero
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class PasajeroActualizar(SuccessMessageMixin, UpdateView):
    model = Pasajero
    form = Pasajero
    fields = "__all__"
    success_message = 'Pasajero Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Pasajero

    # Redireccionamos a la página principal luego de actualizar un registro o pasajero
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class PasajeroEliminar(SuccessMessageMixin, DeleteView):
    model = Pasajero
    form = Pasajero
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o pasajero
    def get_success_url(self):
        success_message = 'Pasajero Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Pasajero
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
