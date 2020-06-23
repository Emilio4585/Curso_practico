from django.shortcuts import render, HttpResponse
from datetime import datetime
from apps.web_personal.web_personal.models import User, Projects, Skills
from django.forms.models import model_to_dict
import json


# Create your views here.


def index(request):
    users = [model_to_dict(ele) for ele in User.objects.all()]
    if len(users) >= 1:
        users = users[0]
    projects = [model_to_dict(ele) for ele in Projects.objects.all()]
    skills = [model_to_dict(ele) for ele in Skills.objects.all()]
    contexto = {'user': users, 'projects': projects, 'skills': skills}
    return render(request, 'web_personal/index.html', context=contexto)
