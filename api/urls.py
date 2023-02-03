from django.urls import path
from .views import product_list, product_detail, category_detail

urlpatterns = [
    path("product/list/", product_list),
    path("product/detail/<str:pk>", product_detail),
]

urlpatterns += [
    path('category/<str:pk>/', category_detail, name='category-detail')
]
