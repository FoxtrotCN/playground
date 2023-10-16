from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Category, Order, OrderItem

# Create your views here.


def say_hello(request):
    # Filtering Exercises

    # Customers with .com accounts
    customer_with_dotcom_accounts = Customer.objects.filter(email__endswith='.com')

    # Categories that don't have a featured product
    categories_without_featured_product = Category.objects.filter(featured_product__isnull=True)

    # Products with low stock
    products_with_low_stock = Product.objects.filter(stock__lt=10)

    # Orders placed by customer with id=1
    orders_placed_by_customer1 = Order.objects.filter(customer__id=1)

    # Order items for products in category 3
    order_items_for_products_in_category3 = OrderItem.objects.filter(product__category__id=3)
    return render(request, 'hello.html', {'orderitems': order_items_for_products_in_category3})
