from django.urls import path

from .views import ListadoClientes, DetallePostre, CrearCliente, ActualizarCliente, EliminarCliente

urlpatterns = [
    path('clientes/', ListadoClientes.as_view(template_name="clientes/index.html"), name='leer'),
    path('clientes/detalle/<int:pk>', DetallePostre.as_view(template_name="clientes/detalles.html"), name='detalles'),
    path('clientes/crear', CrearCliente.as_view(template_name="clientes/crear.html"), name='crear'),
    path('clientes/editar/<int:pk>', ActualizarCliente.as_view(template_name="clientes/actualizar.html"),
         name='actualizar'),
    path('clientes/eliminar/<int:pk>', EliminarCliente.as_view(), name='eliminar'),
]
