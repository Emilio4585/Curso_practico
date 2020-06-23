from django.urls import path

from apps.proyectos.renta_coches.rutas.views import RutaListado, RutaDetalle, RutaCrear, RutaActualizar, RutaEliminar

urlpatterns = [
    path('ruta/', RutaListado.as_view(template_name="proyectos/renta_coches/rutas/index.html"), name='leer'),
    path('ruta/detalle/<int:pk>', RutaDetalle.as_view(template_name="proyectos/renta_coches/rutas/detalles.html"),
         name='detalles'),
    path('ruta/crear', RutaCrear.as_view(template_name="proyectos/renta_coches/rutas/crear.html"), name='crear'),
    path('ruta/editar/<int:pk>', RutaActualizar.as_view(template_name="proyectos/renta_coches/rutas/actualizar.html"),
         name='actualizar'),
    path('ruta/eliminar/<int:pk>', RutaEliminar.as_view(), name='eliminar'),
]
