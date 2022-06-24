from xml.etree.ElementInclude import include
from django import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
