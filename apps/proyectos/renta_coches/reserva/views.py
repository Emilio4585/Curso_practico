from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reserva

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms


class ReservaListado(ListView):
    model = Reserva


class ReservaDetalle(DetailView):
    model = Reserva


class ReservaCrear(SuccessMessageMixin, CreateView):
    model = Reserva
    form = Reserva
    fields = "__all__"
    success_message = 'Reserva Creado Correctamente !'  # Mostramos este Mensaje luego de Crear un Reserva

    # Redireccionamos a la página principal luego de crear un registro o reserva
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ReservaActualizar(SuccessMessageMixin, UpdateView):
    model = Reserva
    form = Reserva
    fields = "__all__"
    success_message = 'Reserva Actualizado Correctamente !'  # Mostramos este Mensaje luego de Editar un Reserva

    # Redireccionamos a la página principal luego de actualizar un registro o reserva
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class ReservaEliminar(SuccessMessageMixin, DeleteView):
    model = Reserva
    form = Reserva
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o reserva
    def get_success_url(self):
        success_message = 'Reserva Eliminado Correctamente !'  # Mostramos este Mensaje luego de Editar un Reserva
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
