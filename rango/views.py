from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<center><h1 style=color:red;>Rango says hey partner</h1></center>")
