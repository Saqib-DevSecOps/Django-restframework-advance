import status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.models import Product, Category
from api.serializer import ProductSerializer, CategorySerializer


@api_view()
def product_list(request):
    product = Product.objects.select_related('category').all()
    product_serializer = ProductSerializer(product, many=True,context={'request': request})
    return Response(product_serializer.data)


@api_view()
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    product_serializer = ProductSerializer(product)
    return Response(product_serializer.data)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
