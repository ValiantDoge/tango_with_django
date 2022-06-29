from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('addcat/',views.add_category, name='add_category'),
    path('category/<category_name_slug>/', views.show_category, name='show_category'),
]   