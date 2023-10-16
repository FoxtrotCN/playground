from django.shortcuts import render
from django.http import HttpResponse
from store.models import Customer

# Create your views here.


def say_hello(request):
    # Filtering Exercises

    # Customers with .com accounts
    customer_with_dotcom_accounts = Customer.objects.filter(email__endswith='.com')
    return render(request, 'hello.html', {'customers': customer_with_dotcom_accounts})
