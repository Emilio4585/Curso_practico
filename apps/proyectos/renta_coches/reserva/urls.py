from django.urls import path

from apps.proyectos.renta_coches.reserva.views import ReservaListado, ReservaDetalle, ReservaCrear, ReservaActualizar, \
    ReservaEliminar

urlpatterns = [
    path('', ReservaListado.as_view(template_name="proyectos/renta_coches/rutas/index.html"), name='leer'),
    path('reserva/detalle/<int:pk>', ReservaDetalle.as_view(template_name="proyectos/renta_coches/rutas/detalles.html"),
         name='detalles'),
    path('reserva/crear', ReservaCrear.as_view(template_name="proyectos/renta_coches/rutas/crear.html"), name='crear'),
    path('reserva/editar/<int:pk>',
         ReservaActualizar.as_view(template_name="proyectos/renta_coches/rutas/actualizar.html"), name='actualizar'),
    path('reserva/eliminar/<int:pk>', ReservaEliminar.as_view(), name='eliminar'),
]
