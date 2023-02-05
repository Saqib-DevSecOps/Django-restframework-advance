from django.urls import path
from .views import ProductListCreateView,ProductUpdateDeleteView,CategoryListCreateView,CategoryUpdateDeleteView

urlpatterns = [
    path("product/", ProductListCreateView.as_view()),
    path("product/detail/<str:pk>", ProductUpdateDeleteView.as_view()),
]

urlpatterns += [
    path('category/', CategoryListCreateView.as_view(), name='category-list'),
    path('category/<str:pk>/', CategoryUpdateDeleteView.as_view(), name='category-detail')
]
