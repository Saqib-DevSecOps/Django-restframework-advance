from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.views import APIView

from api.models import Product, Category
from api.serializer import ProductSerializer, CategorySerializer


class ProductApi(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            product = Product.objects.get(id=pk)
            product = ProductSerializer(product)
            return Response(product.data)
        students = Product.objects.all()
        serializer = ProductSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Succesfully Update'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Succesfully Update'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response({'Msg': 'Successfully Deleted'}, status=status.HTTP_400_BAD_REQUEST)


class ProductList(GenericAPIView, ListModelMixin):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetail(GenericAPIView, RetrieveModelMixin):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductCreate(GenericAPIView, CreateModelMixin):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProductDelete(GenericAPIView, DestroyModelMixin):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryList(GenericAPIView, ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryDetail(GenericAPIView, RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryCreate(GenericAPIView, CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CategoryDelete(GenericAPIView, DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)