from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):  
    # params={'no_of_slides':nslides, 'range':range(1,nslides), 'product':products}

    # allProds = [[products, range(1,nslides), nslides],[products, range(1,nslides), nslides]]
        
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = { item["category"] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n= len(prod)
        nslides = n//4 + ceil ((n/4)-(n//4))
        allProds.append([prod, range(1,nslides), nslides])
    
    params = {"allProds":allProds}
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