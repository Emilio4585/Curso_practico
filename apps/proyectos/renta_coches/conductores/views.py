from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Conductor

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms


class ConductorListado(ListView):
    model = Conductor


class ConductorDetalle(DetailView):
    model = Conductor


class ConductorCrear(SuccessMessageMixin, CreateView):
    model = Conductor
    form = Conductor
    fields = "__all__"
    success_message = 'Conductor Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Conductor

    # Redireccionamos a la página principal luego de crear un registro o conductor
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ConductorActualizar(SuccessMessageMixin, UpdateView):
    model = Conductor
    form = Conductor
    fields = "__all__"
    success_message = 'Conductor Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Conductor

    # Redireccionamos a la página principal luego de actualizar un registro o conductor
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ConductorEliminar(SuccessMessageMixin, DeleteView):
    model = Conductor
    form = Conductor
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o conductor
    def get_success_url(self):
        success_message = 'Conductor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Conductor
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
