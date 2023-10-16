from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):
    # Products: Stock < 10 or Price < 20 | Using the Q object that stands for Query
    queryset = Product.objects.filter(Q(stock__lt=10) | Q(price__lt=20))
    return render(request, 'hello.html', {'products': queryset})
