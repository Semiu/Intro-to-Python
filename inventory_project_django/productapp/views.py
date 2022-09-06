from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from productapp.models import ProductApp


def add_product(request):
    return render(request, 'add.html', None)


def product_list(request):
    # query set object - The .object is the ORM interface and is based on the db used
    # context data is the queryset to be rendered as dict object
    queryset = ProductApp.objects.all()
    return render(request, 'list.html', {'Products': queryset})
    # return HttpResponse(queryset)


def get_product(request, product_id):
    # query set object - The .object is the ORM interface and is based on the db used
    # context data is the queryset to be rendered as dict object
    queryset = ProductApp.objects.filter(id=product_id)
    return render(request, 'product.html', {'Products': queryset})
    # return HttpResponse(queryset)


def del_product(request):
    return render(request, 'delete.html', None)


def home(request):
    return render(request, 'home.html', None)
