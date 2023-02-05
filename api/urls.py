from django.urls import path
from .views import ProductListTCreateApiView, ProductRetrieveUpdateDeleteApiView, \
    CategoryRetrieveUpdateDeleteApiView, CategoryListTCreateApiView

urlpatterns = [
    path("product/", ProductListTCreateApiView.as_view()),
    path("product/detail/<str:pk>", ProductRetrieveUpdateDeleteApiView.as_view()),
]

urlpatterns += [
    path('category/', CategoryListTCreateApiView.as_view(), name='category-list'),
    path('category/<str:pk>/', CategoryRetrieveUpdateDeleteApiView.as_view(), name='category-detail')
]
