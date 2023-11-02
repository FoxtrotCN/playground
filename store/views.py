from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import ProductSerializer, CategorySerializer


@api_view()
def product_list(request):
    products = Product.objects.select_related('category').all()
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    return Response(data)


@api_view()
def product_detail(request, _id):
    # try:
    #
    #     product = Product.objects.get(pk=_id)
    #     serializer = ProductSerializer(product)
    #     data = serializer.data
    #     return Response(data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    product = get_object_or_404(Product, pk=_id)
    serializer = ProductSerializer(product)
    data = serializer.data
    return Response(data)


@api_view()
def category_detail(request, _id):
    category = get_object_or_404(Category, pk=_id)
    serializer = CategorySerializer(category)
    data = serializer.data
    return Response("ok")
