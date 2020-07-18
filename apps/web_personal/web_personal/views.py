from django.shortcuts import render, HttpResponse
from datetime import datetime
from apps.web_personal.web_personal.models import User, Projects, Skills
from django.forms.models import model_to_dict
from django.views.generic.base import RedirectView, TemplateView

import json


# Create your views here.
class Redireccion(RedirectView):
    url = 'index'  # Url redireccionada
    permanent = False  #
    query_string = True  #
    pattern_name = 'redireccion-web'


class Index(TemplateView):
    template_name = "web_personal/index.html"

    def get_context_data(self, **kwargs):
        # users = [model_to_dict(ele) for ele in User.objects.all()]
        user = model_to_dict(User.objects.get(name='Emilio Rafael'))
        projects = [model_to_dict(ele) for ele in Projects.objects.all()]
        skills = [model_to_dict(ele) for ele in Skills.objects.all()]
        contexto = {'user': user, 'projects': projects, 'skills': skills}
        return contexto
