from django.shortcuts import render
from apps.home.models import Setting
from apps.product.models import Category

# Create your views here.
def index(request):
    set = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'settings': set,
        'category': category,
    }
    return render(request, 'index.html', context)


def about_page(request):
    set = Setting.objects.get(pk=1)
    context = {
        'settings': set,
    }
    return render(request, 'about_page.html', context)


def contact_page(request):
    set = Setting.objects.get(pk=1)
    context = {
        'settings': set,
    }
    return render(request, 'contact_page.html', context)