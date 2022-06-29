from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import CategoryForm
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm, PageForm

def index(request):
    category_list= Category.objects.order_by("-likes")[:5]
    pages_list = Page.objects.order_by("-views")[:5]
    form = PageForm()
    context_dict= {'categories': category_list, 'pages':pages_list, 'form':form}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict={}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages= Page.objects.filter(category=category)
        context_dict['pages']=pages
        context_dict['category']=category
    except Category.DoesNotExist:
        context_dict['pages']=None
        context_dict['category']=None
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})
