from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):
    queryset = Product.objects.values_list('id', 'title', 'category__title')

    """
        Exercise: Select Products that have been ordered
                  and sort them by title
    """

    ordered_products = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    return render(request, 'hello.html', {'products': ordered_products})
