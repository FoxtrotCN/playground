from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):


    """
        Exercise: Get the last 5 orders with their customer
                  and items (incl product)
    """
    result = Product.objects.aggregate(Count('id'))
    return render(request, 'hello.html', {'result': result})
