from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path("<pk>/" ,InvoiceViewApi.as_view() , name = "detail" ),
    path("" , InvoiceCreateViewApi.as_view() , name = "create")
]