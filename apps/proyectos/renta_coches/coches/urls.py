from django.urls import path

from apps.proyectos.renta_coches.coches.views import CochesListado, CochesDetalle, CochesCrear, CochesActualizar, \
    CochesEliminar

urlpatterns = [
    path('coches/', CochesListado.as_view(template_name="proyectos/renta_coches/rutas/index.html"), name='leer_coche'),
    path('coche/detalle/<int:pk>', CochesDetalle.as_view(template_name="proyectos/renta_coches/rutas/detalles.html"),
         name='detalles_coche'),
    path('coche/crear', CochesCrear.as_view(template_name="proyectos/renta_coches/rutas/crear.html"),
         name='crear_coche'),
    path('coche/editar/<int:pk>',
         CochesActualizar.as_view(template_name="proyectos/renta_coches/rutas/actualizar.html"),
         name='actualizar_coche'),
    path('coche/eliminar/<int:pk>', CochesEliminar.as_view(), name='eliminar_coche'),
]
