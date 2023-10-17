from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, Func, F, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer, Category, Order, OrderItem


# Create your views here.


def say_hello(request):
    discounted_price = ExpressionWrapper(F('price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price=discounted_price
    )
    return render(request, 'hello.html', {'queryset': list(queryset)})
