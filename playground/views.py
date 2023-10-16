from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):
    # 0, 1, 2, 3, 4
    queryset = Product.objects.all()[:5]
    # 5, 6, 7, 8, 9
    queryset2 = Product.objects.all()[5:10]
    return render(request, 'hello.html', {'products': queryset})
