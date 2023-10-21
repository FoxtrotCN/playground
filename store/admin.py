from django.contrib import admin
from django.db.models import Count, QuerySet
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


class StockFiltering(admin.SimpleListFilter):
    title = 'Stock'
    parameter_name = 'stock'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(stock__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_stock']
    list_display = ['title', 'price', 'stock_status', 'category_title']
    list_editable = ['price']
    list_filter = ['category', 'last_update', StockFiltering]
    list_per_page = 10
    list_select_related = ['category']

    def category_title(self, product):
        return product.category.title

    @admin.display(ordering='stock')
    def stock_status(self, product):
        if product.stock < 10:
            return "Low"
        return "Ok"

    @admin.action(description='Clear Stock')
    def clear_stock(self, request, queryset: QuerySet):
        update_count = queryset.update(stock=0)
        self.message_user(request, f"{update_count} products were successfully updated.")



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

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
