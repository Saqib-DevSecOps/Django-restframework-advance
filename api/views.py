from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, \
    UpdateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from api.filters import ProductFilter
from api.models import Product, Category, Review
from api.pagination import CustomPagination
from api.serializer import CategorySerializers, ProductsSerializers, ReviewSerializer
from rest_framework.pagination import PageNumberPagination


# class ProductApi(APIView):
#     def get(self, request, pk=None):
#         id = pk
#         if id is not None:
#             product = Product.objects.get(id=pk)
#             product = ProductSerializer(product)
#             return Response(product.data)
#         students = Product.objects.all()
#         serializer = ProductSerializer(students, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None, format=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Succesfully Update'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk=None, format=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product, request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Succesfully Update'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         product.delete()
#         return Response({'Msg': 'Successfully Deleted'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductList(GenericAPIView, ListModelMixin):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class ProductDetail(GenericAPIView, RetrieveModelMixin):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
# class ProductCreate(GenericAPIView, CreateModelMixin):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ProductUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
# class ProductDelete(GenericAPIView, DestroyModelMixin):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class CategoryList(GenericAPIView, ListModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class CategoryDetail(GenericAPIView, RetrieveModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
# class CategoryCreate(GenericAPIView, CreateModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class CategoryUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
# class CategoryDelete(GenericAPIView, DestroyModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# Generic View

# Products

class ProductListAPi(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers


class ProductDetailAPi(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers


class ProductUpdateAPi(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers


class ProductCreateApi(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers


class ProductDeleteApi(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers


# Category

class CategoryListApi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailApi(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryCreateAPi(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryUpdateApi(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDeleteApi(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


# Generic View

# If we Want to Customize our detail in Generic View ........

class ProductLists(ListAPIView):

    def get_queryset(self):
        product = Product.objects.select_related('collection').object.all()
        category = self.request.query_params.get['collection_id']
        if category is not None:
            product.filter(category__id=category)
        return product

    def get_serializer_class(self):
        return ProductsSerializers

    def get_serializer_context(self):
        return self.request


class ProductDetails(RetrieveAPIView):

    def get_queryset(self):
        return Product.objects.select_related('category').all()

    def get_serializer_class(self):
        return ProductsSerializers

    def get_serializer_context(self):
        return self.request


class ProductUpdates(UpdateAPIView):

    def get_queryset(self):
        return Product.objects.select_related('category').all()

    def get_serializer_class(self):
        return ProductsSerializers

    def get_serializer_context(self):
        return self.request


class ProductCreates(CreateAPIView):

    def get_queryset(self):
        return Product.objects.select_related('category').all()

    def get_serializer_class(self):
        return ProductsSerializers

    def get_serializer_context(self):
        return self.request


class ProductDeletes(DestroyAPIView):

    def get_queryset(self):
        return Product.objects.select_related('category').all()

    def get_serializer_class(self):
        return ProductsSerializers

    def get_serializer_context(self):
        return self.request


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductsSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['title']
    # filterset_fields = ['title','category']
    pagination_class = CustomPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ReviewModelViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
