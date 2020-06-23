from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coches

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms


class CochesListado(ListView):
    model = Coches


class ConductorDetalle(DetailView):
    model = Coches


class ConductorCrear(SuccessMessageMixin, CreateView):
    model = Coches
    form = Coches
    fields = "__all__"
    success_message = 'Conductor Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Conductor

    # Redireccionamos a la página principal luego de crear un registro o coche
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ConductorActualizar(SuccessMessageMixin, UpdateView):
    model = Coches
    form = Coches
    fields = "__all__"
    success_message = 'Conductor Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Conductor

    # Redireccionamos a la página principal luego de actualizar un registro o coche
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ConductorEliminar(SuccessMessageMixin, DeleteView):
    model = Coches
    form = Coches
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o coche
    def get_success_url(self):
        success_message = 'Conductor Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Conductor
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
