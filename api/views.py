import status
from rest_framework import response, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product, Category
from api.serializer import ProductSerializer, CategorySerializer, ProductMSerializer

"""--------------------Product Api View--------------------"""


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == "GET":
        product = Product.objects.select_related('category').all()
        product_serializer = ProductMSerializer(product, many=True, context={'request': request})
        return Response(product_serializer.data)
    elif request.method == "POST":
        product = ProductMSerializer(data=request.data)
        product.is_valid(raise_exception=True)
        product.save()
        return Response(product.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        product_serializer = ProductMSerializer(product)
        return Response(product_serializer.data)
    elif request.method == "PUT":
        product_serializer = ProductMSerializer(product, data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "PATCH":
        product_serializer = ProductMSerializer(product, data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        product.delete()
        product.save()
        return Response(status=status.HTTP_200_OK)


"""-----------------------------------------------------------"""

"""--------------------Category Api View--------------------"""


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        category = CategorySerializer(data=request.data)
        category.is_valid(raise_exception=True)
        category.save()
        return Response(category.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    if request.method == "GET":
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)
    elif request.method == "PUT":
        category_serializer = CategorySerializer(category, data=request.data)
        category_serializer.is_valid(raise_exception=True)
        category_serializer.save()
        return Response(category_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "PATCH":
        category_serializer = CategorySerializer(category, data=request.data)
        category_serializer.is_valid(raise_exception=True)
        category_serializer.save()
        return Response(category_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        category.delete()
        category.save()
        return Response(status=status.HTTP_200_OK)


"""-----------------------------------------------------------"""

"""--------------------Product Class Based View--------------------"""


class ProductList(APIView):
    def get(self, request):
        product = Product.objects.select_related('category').all()
        product_serializer = ProductMSerializer(product, many=True, context={'request': request})
        return Response(product_serializer.data)

    def post(self, request):
        product = ProductMSerializer(data=request.data)
        product.is_valid(raise_exception=True)
        product.save()
        return Response(product.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product_serializer = ProductMSerializer(product)
        return Response(product_serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product_serializer = ProductMSerializer(product, data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product_serializer = ProductMSerializer(product, data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        product.save()
        return Response(status=status.HTTP_200_OK)


"""-----------------------------------------------------------"""

"""--------------------Category Class Based View--------------------"""


class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()
        category_serializer = CategorySerializer(category, many=True, context={'request': request})
        return Response(category_serializer.data)

    def post(self, request):
        category = CategorySerializer(data=request.data)
        category.is_valid(raise_exception=True)
        category.save()
        return Response(category.data, status=status.HTTP_201_CREATED)


class CategoryDetail(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category_serializer = CategorySerializer(category, data=request.data)
        category_serializer.is_valid(raise_exception=True)
        category_serializer.save()
        return Response(category_serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category_serializer = CategorySerializer(category, data=request.data)
        category_serializer.is_valid(raise_exception=True)
        category_serializer.save()
        return Response(category_serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        category.save()
        return Response(status=status.HTTP_200_OK)


"""-----------------------------------------------------------"""

"""--------------------Product Mixin View--------------------"""


class ProductListCreateView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            GenericAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductMSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductUpdateDeleteView(mixins.UpdateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin,
                              GenericAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductMSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""------------------------------------------------------------------"""

"""--------------------Category Mixin View--------------------"""


class CategoryListCreateView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryUpdateDeleteView(mixins.UpdateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.DestroyModelMixin,
                               GenericAPIView):
    queryset = Category.objects.select_related('category').all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""------------------------------------------------------------------"""

"""--------------------Product GENERIC API View--------------------"""


class ProductListTCreateApiView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductMSerializer


class ProductRetrieveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductMSerializer


"""------------------------------------------------------------------"""

"""--------------------Category GENERIC API View--------------------"""


class CategoryListTCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


"""------------------------------------------------------------------"""
