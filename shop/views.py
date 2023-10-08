from math import ceil
from django.shortcuts import render,HttpResponse
from .models import Product,Contact,Order,OrderUpdate
import json

# Create your views here.

def index(request):  

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



def checkout(request):
    thank =False
    id_ = None
    if request.method =="POST" :
        items_json=request.POST.get('itemJson',"")
        name = request.POST.get('name',"")
        email= request.POST.get('email','')
        phone = request.POST.get('phone',"")
        address = request.POST.get('address1',"") + "" + request.POST.get("address2","")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip_code = request.POST.get('zip_code',"")
        amount = request.POST.get('amount',"")

        order = Order(items_json=items_json, name=name , email=email, address=address, phone=phone,city=city, state=state, zip_code=zip_code, amount=amount)
        order.save()
        update=OrderUpdate(order_id = order.order_id , update_decs =f"Dear {name} Your order is placed")
        update.save()
    
        thank =True
        id_ = order.order_id

        
    print(id_)
    return render(request , 'shop/checkout.html',{'thank':thank, 'id':id_})



def tracker(request):
    if request.method =="POST" :
        orderId = request.POST.get('orderId',"")
        email = request.POST.get('email',"")
        
        try:
            order = Order.objects.filter(order_id=orderId, email= email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates=[]

                for item in update:
                    updates.append({'text':item.update_decs, 'time':item.timetamp})
                    responce = json.dumps(updates,default=str)
                return HttpResponse(responce)
            else:
                return HttpResponse({})
        except Exception as e:
            return HttpResponse({})



    return render(request , 'shop/tracker.html')







def search(request):
    return render(request , 'shop/search.html')

  
