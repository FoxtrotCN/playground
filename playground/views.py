from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):


    """
        Aggregating Exercises:
    """
    # How many orders do we have?
    result = Order.objects.aggregate(count=Count('id'))

    # How many units of product 1 have we sold?
    result = OrderItem.objects.filter(product__id=1).aggregate(units_sold=Sum('quantity'))

    # How many orders has customer 1 placed?
    result = Order.objects.filter(customer__id=1).aggregate(orders_placed=Count('id'))

    return render(request, 'hello.html', {'result': result})
