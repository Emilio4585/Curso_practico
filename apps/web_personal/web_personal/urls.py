from django.contrib import admin
from django.urls import path
from apps.web_personal.web_personal.views import index

urlpatterns = [
    path('index/', index, name='index'),
]
