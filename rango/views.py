from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict= {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("<center><h1>Rango says here is the about page.<br></h1><br><a href='/rango/'>Rango</a></h1></center>")

