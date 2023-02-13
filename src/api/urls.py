from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import ProductListCreateApiView, ProductRetrieveUpdateDeleteApiView, \
    CategoryRetrieveUpdateDeleteApiView, CategoryListCreateApiView, ProductViewSet, CategoryViewSet, ReviewModelViewSet, \
    CartModelViewSet, CartItemModelViewSet, CartItemListVIew, CartItemRUDVIew, OrderItemModelViewSet, OrderModelViewSet

# urlpatterns = [
#     path("product/", ProductListCreateApiView.as_view()),
#     path("product/detail/<str:pk>", ProductRetrieveUpdateDeleteApiView.as_view()),
# ]
#
# urlpatterns += [
#     path('category/', CategoryListCreateApiView.as_view(), name='category-list'),
#     path('category/<str:pk>/', CategoryRetrieveUpdateDeleteApiView.as_view(), name='category-detail')
# ]
#
# urlpatterns += [
#     path('cart/<str:cart_pk>/item/', CartItemListVIew.as_view()),
#     path('cart/<str:cart_pk>/item/<str:pk>', CartItemRUDVIew.as_view())
# ]
"""__________________ROUTERS FOR MODEL VIEWSET_____________________"""

router = DefaultRouter()
# base name is used for get the specific url like for product products-list,products-detail,etc
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('carts', CartModelViewSet, basename='carts')
router.register('order', OrderModelViewSet, basename='order')
urlpatterns = router.urls

"""------------------DRF NESTED ROUTER------------------------------"""

product_router = NestedSimpleRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewModelViewSet, basename='product-reviews')

cart_router = NestedSimpleRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemModelViewSet, basename='cart-items')

order_item_router = NestedSimpleRouter(router, 'order', lookup='order')
order_item_router.register('order-items', OrderItemModelViewSet, basename='order=item')

urlpatterns += product_router.urls
urlpatterns += cart_router.urls
urlpatterns += order_item_router.urls
