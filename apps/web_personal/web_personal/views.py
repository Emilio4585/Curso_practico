from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request


def index(request):
    return render(request, 'web_personal/index.html', context=None)


def about(request):
    return render(request, 'web_personal/about.html', context=None)


def contact(request):
    return render(request, 'web_personal/contact.html', context=None)


def portafolio(request):
    return render(request, 'web_personal/portafolio.html', context=None)
