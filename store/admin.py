from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

from . import models


# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, category):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                    'category__id': str(category.id)
                }))
        return format_html('<a href="{}">{}</a>', url, category.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock_status', 'category_title']
    list_editable = ['price']
    list_per_page = 10
    list_select_related = ['category']

    def category_title(self, product):
        return product.category.title

    @admin.display(ordering='stock')
    def stock_status(self, product):
        if product.stock < 10:
            return "Low"
        return "Ok"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
                reverse('admin:store_order_changelist')
                + '?'
                + urlencode({
            'customer__id': str(customer.id)
        }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'payment_status', 'customer']
    list_per_page = 10
