from django.http import HttpResponse
from django.shortcuts import render
from django.template.backends import django
from django.http import HttpResponse
from .models import product


def index(request):
    products = product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('New Products')

