from django.urls import path
from .views import ProductListCreateApiView, ProductRetrieveUpdateDeleteApiView, \
    CategoryRetrieveUpdateDeleteApiView, CategoryListCreateApiView

urlpatterns = [
    path("product/", ProductListCreateApiView.as_view()),
    path("product/detail/<str:pk>", ProductRetrieveUpdateDeleteApiView.as_view()),
]

urlpatterns += [
    path('category/', CategoryListCreateApiView.as_view(), name='category-list'),
    path('category/<str:pk>/', CategoryRetrieveUpdateDeleteApiView.as_view(), name='category-detail')
]
