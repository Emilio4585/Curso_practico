from django.urls import path

from apps.proyectos.renta_coches.conductores.views import ConductorListado, ConductorDetalle, ConductorCrear, \
    ConductorActualizar, ConductorEliminar

urlpatterns = [
    path('conductores/', ConductorListado.as_view(template_name="proyectos/renta_coches/rutas/index.html"),
         name='leer'),
    path('conductores/detalle/<int:pk>',
         ConductorDetalle.as_view(template_name="proyectos/renta_coches/rutas/detalles.html"), name='detalles'),
    path('conductores/crear', ConductorCrear.as_view(template_name="proyectos/renta_coches/rutas/crear.html"),
         name='crear'),
    path('conductores/editar/<int:pk>',
         ConductorActualizar.as_view(template_name="proyectos/renta_coches/rutas/actualizar.html"), name='actualizar'),
    path('conductores/eliminar/<int:pk>', ConductorEliminar.as_view(), name='eliminar'),
]
