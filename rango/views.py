from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<center><h1 style=color:red;>Rango says hey partner</h1><br><a href='/rango/about/'>About</a></center>")


def about(request):
    return HttpResponse("<center><h1>Rango says here is the about page.<br></h1><br><a href='/rango/'>Rango</a></h1></center>")

