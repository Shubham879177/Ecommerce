from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n= len(products)
    nslides = n//4 + ceil ((n/4)-(n//4))
    params={'no_of_slides':nslides, 'range':range(1,nslides), 'product':products}
    return render(request , 'shop/index.html',params) 

def about(request):
    # return HttpResponse("Hi i am about")
    return render(request , 'shop/about.html') 

def contact(request):
    return HttpResponse("Hi i am contact")
    # return render(request , 'shop/index.html') 

def tracker(request):
    return HttpResponse("Hi i am tracker")
    # return render(request , 'shop/index.html')

def search(request):
    return HttpResponse("Hi i am search")
    # return render(request , 'shop/index.html')

def prodview(request):
    return HttpResponse("Hi i am productview")
    # return render(request , 'shop/index.html') 

def checkout(request):
    return HttpResponse("Hi i am checkout")
    # return render(request , 'shop/index.html') 