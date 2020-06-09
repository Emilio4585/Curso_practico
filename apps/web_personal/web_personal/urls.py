from django.contrib import admin
from django.urls import path
from apps.web_personal.web_personal.views import index, about, contact, portafolio

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('portafolio/', portafolio, name='portafolio'),
]
