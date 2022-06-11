from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register('student',views.ProductModelViewSet,basename='product')
router.register('category',views.CategoryModelViewSet,basename='category')
urlpatterns = [
    path('',include(router.urls))

    # # path('', views.ProductApi.as_view(), name='products'),
    # # path('/<str:pk>/', views.ProductApi.as_view(), name='products'),
    #
    # path('', views.ProductListAPi.as_view(), name='products'),
    # path('product/<str:pk>/', views.ProductDetailAPi.as_view(), name='products'),
    # path('create/', views.ProductCreateApi.as_view(), name='product_create'),
    # path('update/<str:pk>/', views.ProductUpdateAPi.as_view(), name='product_update'),
    # path('delete/<str:pk>/', views.ProductDeleteApi.as_view(), name='product_delete'),
    # path('category', views.CategoryListApi.as_view(), name='categories'),
    # path('category/<str:pk>/', views.CategoryDetailApi.as_view(), name='category'),
    # path('category/create/', views.CategoryCreateAPi.as_view(), name='category_create'),
    # path('category/update/<str:pk>/', views.CategoryUpdateApi.as_view(), name='category_update'),
    # path('category/delete/<str:pk>/', views.CategoryDeleteApi.as_view(), name='category_delete'),

]
