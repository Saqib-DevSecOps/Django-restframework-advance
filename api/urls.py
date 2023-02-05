from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import ProductListCreateApiView, ProductRetrieveUpdateDeleteApiView, \
    CategoryRetrieveUpdateDeleteApiView, CategoryListCreateApiView, ProductViewSet, CategoryViewSet, ReviewModelViewSet

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
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
product_router = NestedSimpleRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewModelViewSet, basename='product-reviews')
urlpatterns += router.urls
urlpatterns += product_router.urls
