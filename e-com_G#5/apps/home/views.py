from django.shortcuts import render
from apps.home.models import Setting
from apps.product.models import Category, Product

# Create your views here.
def index(request):
    set = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('id')[:3]
    product_lastet = Product.objects.all().order_by('-id')[:4]
    product_picked = Product.objects.all().order_by('?')[:4]
    context = {
        'settings': set,
        'category': category,
        'product_slider' :  product_slider,
        'product_slider' :  product_lastet,
        'product_slider' :  product_picked,
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