from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, Func, F, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer, Category, Order, OrderItem


# Create your views here.


def say_hello(request):
    # Annotating Exercises

    # Customers with their last order ID
    queryset = Customer.objects.annotate(last_order_id=Max('order__id'))

    # Categories and count of their products
    queryset = Category.objects.annotate(products_count=Count('product'))
    return render(request, 'hello.html', {'queryset': list(queryset)})
