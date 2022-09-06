from django.urls import path
from .views import add_product, del_product, product_list, home

urlpatterns = [
    path("", home),
    path("addproduct", add_product),
    path("deleteproduct", del_product),
    path("listproduct", product_list)
]