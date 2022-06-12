from decimal import Decimal

from rest_framework import serializers

from api.models import Product, Category, Review


#
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100)
#     # category = serializers.StringRelatedField()
#     category = CategorySerializers()
#     unit_price = serializers.DecimalField(max_digits=8, decimal_places=2, source='price')
#     tax_price = serializers.SerializerMethodField(method_name='calculated_tax')
#
#     def calculated_tax(self, product: Product):
#         return product.price * Decimal(1.5)
#     #
#     # def create(self, validated_data):
#     #     return Product.objects.create(**validated_data)
#     #
#     # def update(self, instance, validated_data):
#     #     instance.title = validated_data.get('title', instance.title)
#     #     instance.category = validated_data.get('category', instance.category)
#     #     instance.price = validated_data.get('price', instance.price)
#     #
#     #     instance.save()
#     #     return instance


class CategorySerializers(serializers.Serializer):
    title = serializers.CharField(max_length=200)


class ProductsSerializers(serializers.ModelSerializer):
    tax_price = serializers.SerializerMethodField(method_name='calculated_tax')
    # category = serializers.StringRelatedField(many=True,read_only=True,source='category-detail')
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='price')

    class Meta:
        model = Product
        fields = ['title', 'unit_price', 'tax_price','inventory','category']

    def calculated_tax(self, product: Product):
        return product.price * Decimal(1.5)


class ReviewSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(read_only=True,many=True,source='')
    class Meta:
        model = Review
        fields = ['product','name','description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id,**validated_data)
        return review

