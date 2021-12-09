from django.db.models import query
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from apps.home.models import Setting
from apps.product.models import Category, Product
from apps.home.forms import SearchForm
from apps.product.views import category_product

# Create your views here.
def index(request):
    set = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('id')[:3] #первые 3
    product_latest = Product.objects.all().order_by('-id')[:4] #последние 4
    product_picked = Product.objects.all().order_by('?')[:4] #последние 4
    context = {
        'settings': set,
        'category': category,
        'product_slider': product_slider,
        'product_latest': product_latest,
        'product_random': product_picked,
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


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products=Product.objects.filter(title__icontains=query) # SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)
            
            category = Category.objects.all()
            settings = Setting.objects.get(pk=1)
            context = {
                'products':products,
                'query':query,
                'category':category,
                'settings':settings,
            }
            return render(request, 'search_products.html', context)
    return HttpResponseRedirect('/')