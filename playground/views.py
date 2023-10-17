from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, Func, F
from django.db.models.functions import Concat
from store.models import Product, Customer, Category, Order, OrderItem


# Create your views here.


def say_hello(request):
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    )
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Concat('first_name', Value(' '), 'last_name')
    )
    return render(request, 'hello.html', {'queryset': list(queryset)})
