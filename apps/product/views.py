from django.http.response import HttpResponse
from django.shortcuts import render
from apps.product.models import Product

# Create your views here.
def category_product(request, id, slug):
    product = Product.objects.filter(category_id=id)
    return HttpResponse(product)