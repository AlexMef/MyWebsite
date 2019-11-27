from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'rango/index.html')


def about(request):
    return HttpResponse("<a href='/rango'>Index</a>")
