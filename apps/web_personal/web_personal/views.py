from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.template.context_processors import request


def index(request):
    contexto = {
        'name': 'Emilio Rafael',
        'carrera': 'Ingeniero en Sistemas',
        'fecha': datetime.now().year,
    }
    return render(request, 'web_personal/index.html', context=contexto)


def about(request):
    return render(request, 'web_personal/about.html', context=None)


def contact(request):
    return render(request, 'web_personal/contact.html', context=None)


def portafolio(request):
    return render(request, 'web_personal/portfolio.html', context=None)

def skills(request):
    return render(request, 'web_personal/skills.html', context=None)

