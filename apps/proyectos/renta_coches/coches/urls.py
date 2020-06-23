from django.urls import path

from apps.proyectos.renta_coches.coches.views import CochesListado, CochesDetalle, CochesCrear, CochesActualizar, \
    CochesEliminar

urlpatterns = [
    path('coches/', CochesListado.as_view(template_name="proyectos/renta_coches/rutas/index.html"), name='leer'),
    path('coche/detalle/<int:pk>', CochesDetalle.as_view(template_name="proyectos/renta_coches/rutas/detalles.html"),
         name='detalles'),
    path('coche/crear', CochesCrear.as_view(template_name="proyectos/renta_coches/rutas/crear.html"), name='crear'),
    path('coche/editar/<int:pk>',
         CochesActualizar.as_view(template_name="proyectos/renta_coches/rutas/actualizar.html"), name='actualizar'),
    path('coche/eliminar/<int:pk>', CochesEliminar.as_view(), name='eliminar'),
]
