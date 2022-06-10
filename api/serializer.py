from decimal import Decimal

from rest_framework import serializers

from api.models import Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    # category = serializers.StringRelatedField()
    category = CategorySerializer()
    unit_price = serializers.DecimalField(max_digits=8, decimal_places=2, source='price')
    tax_price = serializers.SerializerMethodField(method_name='calculated_tax')

    def calculated_tax(self, product: Product):
        return product.price * Decimal(1.5)
    #
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.price = validated_data.get('price', instance.price)
    #
    #     instance.save()
    #     return instance


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ['title','unit_price', 'tax_price','category']

    tax_price = serializers.SerializerMethodField(method_name='calculated_tax')

    def calculated_tax(self, product: Product):
        return product.price * Decimal(1.5)
    category = CategorySerializer()
