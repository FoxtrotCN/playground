from decimal import Decimal
from rest_framework import serializers

from store.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_taxes', 'category']

    price_with_taxes = serializers.SerializerMethodField(method_name='tax_calculation')

    def tax_calculation(self, product: Product):
        return product.price * Decimal(1.1)

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # category = serializers.StringRelatedField()
