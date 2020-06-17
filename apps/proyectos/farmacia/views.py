from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'proyectos/farmacia/index.html')


def index2(request):
    return render(request, 'proyectos/farmacia/index2.html')


def index3(request):
    return render(request, 'proyectos/farmacia/index3.html')


def index4(request):
    return render(request, 'proyectos/farmacia/index4.html')


def alert(request):
    return render(request, 'proyectos/farmacia/alert.html')


def badge(request):
    return render(request, 'proyectos/farmacia/badge.html')


def button(request):
    return render(request, 'proyectos/farmacia/button.html')


def card(request):
    return render(request, 'proyectos/farmacia/card.html')


def chart(request):
    return render(request, 'proyectos/farmacia/chart.html')


def fontawesome(request):
    return render(request, 'proyectos/farmacia/fontawesome.html')


def forget_pass(request):
    return render(request, 'proyectos/farmacia/forget-pass.html')


def form(request):
    return render(request, 'proyectos/farmacia/form.html')


def grid(request):
    return render(request, 'proyectos/farmacia/grid.html')


def inbox(request):
    return render(request, 'proyectos/farmacia/inbox.html')


def login(request):
    return render(request, 'proyectos/farmacia/login.html')


def map(request):
    return render(request, 'proyectos/farmacia/map.html')


def modal(request):
    return render(request, 'proyectos/farmacia/modal.html')


def progress_bar(request):
    return render(request, 'proyectos/farmacia/progress-bar.html')


def register(request):
    return render(request, 'proyectos/farmacia/register.html')


def switch(request):
    return render(request, 'proyectos/farmacia/switch.html')


def tab(request):
    return render(request, 'proyectos/farmacia/tab.html')


def table(request):
    return render(request, 'proyectos/farmacia/table.html')


def typo(request):
    return render(request, 'proyectos/farmacia/typo.html')
