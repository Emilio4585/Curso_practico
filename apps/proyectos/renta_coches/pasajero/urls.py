from django.urls import path

from apps.proyectos.renta_coches.pasajero.views import PasajeroListado, PasajeroDetalle, PasajeroCrear, \
    PasajeroActualizar, PasajeroEliminar

urlpatterns = [
    path('pasajeros/', PasajeroListado.as_view(template_name="proyectos/renta_coches/rutas/index.html"), name='leer'),
    path('pasajeros/detalle/<int:pk>',
         PasajeroDetalle.as_view(template_name="proyectos/renta_coches/rutas/detalles.html"), name='detalles'),
    path('pasajeros/crear', PasajeroCrear.as_view(template_name="proyectos/renta_coches/rutas/crear.html"),
         name='crear'),
    path('pasajeros/editar/<int:pk>',
         PasajeroActualizar.as_view(template_name="proyectos/renta_coches/rutas/actualizar.html"), name='actualizar'),
    path('pasajeros/eliminar/<int:pk>', PasajeroEliminar.as_view(), name='eliminar'),
]
