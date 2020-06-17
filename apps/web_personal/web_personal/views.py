from django.shortcuts import render
from datetime import datetime
from apps.web_personal.web_personal.models import User, Projects, Skills
from django.forms.models import model_to_dict
import json


# Create your views here.


def index(request):
    usuario = model_to_dict(User.objects.get(pk=1))

    proyectos = [model_to_dict(ele) for ele in Projects.objects.all()]

    skills = [model_to_dict(ele) for ele in Skills.objects.all()]

    contexto = {'usuario': usuario, 'proyectos': proyectos, 'skills': skills}
    return render(request, 'web_personal/index.html', context=contexto)
