from abc import ABC
from decimal import Decimal
from rest_framework import serializers

from api.models import Category, Product

"""_______________________Category Serializer_____________________"""


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)


"""________________________PRODUCT SERIALIZER_____________________"""


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    inventory = serializers.IntegerField()
    is_available = serializers.BooleanField(default=True)
    # ________Custom Serializer field________
    price_with_tax = serializers.SerializerMethodField(method_name='tax_calculation')
    # ________PrimaryKey Serializer field________
    category_pk = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    # __________String Serializer field________
    category_str = serializers.StringRelatedField(source='category')
    # ________Nested object Serializer field________
    category = CategorySerializer()
    # ________HyperLink Serializer field________
    category_hyp = serializers.HyperlinkedRelatedField(queryset=Category.objects.all(),
                                                   view_name='category-detail',source='category')

    def tax_calculation(self, product: Product):
        return product.price * Decimal(1.10)
