from django.contrib import admin
from . import models


# Register your models here.

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
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'payment_status', 'customer']
    list_per_page = 10


admin.site.register(models.Category)
