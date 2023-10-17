from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):

    """
        Exercise: Get the last 5 orders with their customer
                  and items (incl product)
    """
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    return render(request, 'hello.html', {'orders': queryset})
