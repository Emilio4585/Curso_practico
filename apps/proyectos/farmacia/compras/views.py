from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Cabecera
from django import forms


class ListadoCompras(ListView):
    model = Compra


class DetallePostre(DetailView):
    model = Compra


class CrearCompra(SuccessMessageMixin, CreateView):
    model = Compra
    form = Compra
    fields = "__all__"
    success_message = 'Compra Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ActualizarCompra(SuccessMessageMixin, UpdateView):
    model = Compra
    form = Compra
    fields = "__all__"
    success_message = 'Compra Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class EliminarCompra(SuccessMessageMixin, DeleteView):
    model = Compra
    form = Compra
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Compra Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
