from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact

# Create your views here.

def index(request):  
    # params={'no_of_slides':nslides, 'range':range(1,nslides), 'product':products}

    # allProds = [[products, range(1,nslides), nslides],[products, range(1,nslides), nslides]]
        
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = { item["category"] for item in catProds}
    for cat in cats:
        product = Product.objects.filter(category=cat)
        n= len(product)
        nslides = n//4 + ceil ((n/4)-(n//4))
        allProds.append([product, range(1,nslides), nslides])
    
    params = {"allProds":allProds}
    return render(request , 'shop/index.html',params) 




def prodview(request,name):

    # fetching the product by its id 
    prod=Product.objects.filter(product_name=name)
 
    return render(request, "shop/prodView.html", {'product':prod[0]})


def about(request):
    # return HttpResponse("Hi i am about")
    return render(request , 'shop/about.html')

def contact(request):
    if request.method =="POST" :
        name = request.POST.get('name',"")
        email= request.POST.get('email','')
        phone = request.POST.get('phone',"")
        query = request.POST.get('query',"")

        # logic for saving the data in database

        contact = Contact(name=name , email=email, phone=phone, desc=query)
        contact.save()

    return render(request , 'shop/contact.html') 

def tracker(request):
    # return HttpResponse("Hi i am tracker")
    return render(request , 'shop/tracker.html')

def search(request):
    return render(request , 'shop/search.html')

  

def checkout(request):
    return render(request , 'shop/checkout.html')
