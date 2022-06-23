from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("We are at about")
    
def contact(request):
    return HttpResponse("We are at contact")
  
def tracker(request):
    return HttpResponse("We are at about")

def productView(request):
    return HttpResponse("We are at product view")
def search(request):
    return HttpResponse("We are at search")
def checkout(request):
    return HttpResponse("We are at checkout")