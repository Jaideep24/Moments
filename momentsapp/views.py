from django.shortcuts import render
from .models import Moment, Cake


def index(request):
    moments = Moment.objects.all()[:20]
    return render(request, 'momentsapp/index.html', {'moments': moments})


def about(request):
    return render(request, 'momentsapp/about.html')


def cakes(request):
    cakes = Cake.objects.all()
    return render(request, 'momentsapp/cakes.html', {'cakes': cakes})


def contact(request):
    return render(request, 'momentsapp/contact.html')
