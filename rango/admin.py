from unicodedata import category
from django.contrib import admin
from rango.models import Category, Page


admin.site.register(Page)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    # Update the registration to include this customised interface

admin.site.register(Category,CategoryAdmin)