from django.urls import path
from .views import product_list, product_detail, category_detail, category_list

urlpatterns = [
    path("product/list/", product_list),
    path("product/detail/<str:pk>", product_detail),
]

urlpatterns += [
    path('category/', category_list, name='category-list'),
    path('category/<str:pk>/', category_detail, name='category-detail')
]
