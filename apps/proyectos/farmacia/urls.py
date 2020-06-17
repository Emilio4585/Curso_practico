from django.contrib import admin
from django.urls import path, include
from apps.proyectos.farmacia.views import *

urlpatterns = [

    path('alert/', alert, name='alert'),
    path('badge/', badge, name='badge'),
    path('button/', button, name='button'),
    path('card/', card, name='card'),
    path('chart/', chart, name='chart'),
    path('fontawesome/', fontawesome, name='fontawesome'),
    path('forget-pass/', forget_pass, name='forget-pass'),
    path('form/', form, name='form'),
    path('grid/', grid, name='grid'),
    path('inbox/', inbox, name='inbox'),
    path('index/', index, name='index'),
    path('index2/', index2, name='index2'),
    path('index3/', index3, name='index3'),
    path('index4/', index4, name='index4'),
    path('login/', login, name='login'),
    path('map/', map, name='map'),
    path('modal/', modal, name='modal'),
    path('progress-bar/', progress_bar, name='progress-bar'),
    path('register/', register, name='register'),
    path('switch/', switch, name='switch'),
    path('tab/', tab, name='tab'),
    path('table/', table, name='table'),
    path('typo/', typo, name='typo'),
]
