from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):
    queryset = Product.objects.values_list('id', 'title', 'category__title')
    return render(request, 'hello.html', {'products': queryset})
