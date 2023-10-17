from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value
from store.models import Product, Customer, Category, Order, OrderItem


# Create your views here.


def say_hello(request):
    queryset = Customer.objects.annotate(is_new=Value(True))
    return render(request, 'hello.html', {'queryset': list(queryset)})
