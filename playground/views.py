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

    # What is the min, max and avg price of products in category 1?
    result = Product.objects.filter(category__id=3).aggregate(min_price=Min('price'), avg_price=Avg('price'), max_price=Max('price'))

    return render(request, 'hello.html', {'result': result})
