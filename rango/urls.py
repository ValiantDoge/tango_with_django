from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
      path('', views.index, name="index"),
      path(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name="show_category")
]