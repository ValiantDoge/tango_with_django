from django.contrib import admin
from django.urls import path
from lol import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home')
]