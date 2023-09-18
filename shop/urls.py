
from . import views
from django.urls import path

urlpatterns = [
   path("",views.index, name="ShopHome"),
   path("about/",views.about, name="AboutUS"),
   path("contact/",views.contact, name="ContactUs"),
   path("tracker/",views.tracker, name="TrackingStatus"),
   path("search/",views.search, name="Search"),
   path("product/<str:name>",views.prodview, name="ProductView"),
   path("checkout/",views.checkout, name="CheckOut"),
]