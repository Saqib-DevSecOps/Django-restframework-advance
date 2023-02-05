from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductListCreateApiView, ProductRetrieveUpdateDeleteApiView, \
    CategoryRetrieveUpdateDeleteApiView, CategoryListCreateApiView, ProductViewSet, CategoryViewSet

urlpatterns = [
    path("product/", ProductListCreateApiView.as_view()),
    path("product/detail/<str:pk>", ProductRetrieveUpdateDeleteApiView.as_view()),
]

urlpatterns += [
    path('category/', CategoryListCreateApiView.as_view(), name='category-list'),
    path('category/<str:pk>/', CategoryRetrieveUpdateDeleteApiView.as_view(), name='category-detail')
]

"""__________________ROUTERS FOR MODEL VIEWSET_____________________"""
router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns += router.urls
