from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:_id>', views.product_detail),
    path('category/<int:_id>', views.category_detail),
]