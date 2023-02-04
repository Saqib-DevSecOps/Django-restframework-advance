from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail

urlpatterns = [
    path("product/", ProductList.as_view()),
    path("product/detail/<str:pk>", ProductDetail.as_view()),
]

urlpatterns += [
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<str:pk>/', CategoryDetail.as_view(), name='category-detail')
]
