from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Category

# Create your views here.


def say_hello(request):
    # Filtering Exercises

    # Customers with .com accounts
    customer_with_dotcom_accounts = Customer.objects.filter(email__endswith='.com')

    # Categories that don't have a featured product
    categories_without_featured_product = Category.objects.filter(featured_product__isnull=True)
    return render(request, 'hello.html', {'categories': categories_without_featured_product})
