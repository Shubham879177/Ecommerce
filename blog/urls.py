
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("",views.blog, name="Blog")
]
