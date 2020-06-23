from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms


class ListadoClientes(ListView):
    model = Cliente


class DetallePostre(DetailView):
    model = Cliente


class CrearCliente(SuccessMessageMixin, CreateView):
    model = Cliente
    form = Cliente
    fields = "__all__"
    success_message = 'Cliente Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ActualizarCliente(SuccessMessageMixin, UpdateView):
    model = Cliente
    form = Cliente
    fields = "__all__"
    success_message = 'Cliente Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class EliminarCliente(SuccessMessageMixin, DeleteView):
    model = Cliente
    form = Cliente
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Cliente Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
