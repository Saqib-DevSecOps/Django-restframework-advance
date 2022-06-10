from django.urls import path

from .import views

urlpatterns = [


    # path('', views.ProductApi.as_view(), name='products'),
    # path('/<str:pk>/', views.ProductApi.as_view(), name='products'),

    path('', views.ProductList.as_view(), name='products'),
    path('product/<str:pk>/', views.ProductDetail.as_view(), name='products'),
    path('create/', views.ProductCreate.as_view(), name='product_create'),
    path('update/<str:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    path('delete/<str:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    path('category', views.CategoryList.as_view(), name='categories'),
    path('category/<str:pk>/', views.CategoryDetail.as_view(), name='category'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/update/<str:pk>/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<str:pk>/', views.CategoryDelete.as_view(), name='category_delete'),

]
