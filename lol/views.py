from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is homepage</h1>")
