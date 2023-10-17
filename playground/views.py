from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, Func, F, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer, Category, Order, OrderItem
from tags.models import TaggedItem


# Create your views here.


def say_hello(request):
    queryset = TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'queryset': list(queryset)})
