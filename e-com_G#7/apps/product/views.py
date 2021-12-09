from django.http.response import HttpResponse
from django.shortcuts import render
from apps.product.models import Product, Category, Images
from apps.home.models import Setting

# Create your views here.
def category_product(request, id, slug):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'settings':settings,
        'category':category,
        'products':products,
        'catdata':catdata,
    }
    return render(request, 'category_products.html', context)



def  product_detail(request, id, slug):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    images = Images.objects.filter(product_id=id)
    context = {
        'settings':settings,
        'category':category,
        'products':products,
        'catdata':catdata,
    }
    return render(request, 'category_products.html', context)


