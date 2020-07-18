from django.urls import path

from apps.proyectos.renta_coches.rutas.views import RutaListado, RutaDetalle, RutaCrear, RutaActualizar, RutaEliminar

urlpatterns = [
    path('ruta/', RutaListado.as_view(template_name="proyectos/renta_coches/rutas/index.html"), name='leer_rutas'),
    path('ruta/detalle/<int:pk>', RutaDetalle.as_view(template_name="proyectos/renta_coches/rutas/detalles.html"),
         name='detalles_ruta'),
    path('ruta/crear', RutaCrear.as_view(template_name="proyectos/renta_coches/rutas/crear.html"), name='crear_ruta'),
    path('ruta/editar/<int:pk>', RutaActualizar.as_view(template_name="proyectos/renta_coches/rutas/actualizar.html"),
         name='actualizar_ruta'),
    path('ruta/eliminar/<int:pk>', RutaEliminar.as_view(), name='eliminar_ruta'),
]
