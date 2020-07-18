from django.urls import path
from apps.web_personal.web_personal.views import Index, Redireccion

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('', Redireccion.as_view(), name='redireccion-web')
]
