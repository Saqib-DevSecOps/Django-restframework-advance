from abc import ABC
from decimal import Decimal
from uuid import uuid4

from rest_framework import serializers

from api.models import Category, Product, Review, Cart, cart_item

"""_______________________Category Serializer_____________________"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', ]

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.save()
        return instance


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
                                                       view_name='category-detail', source='category')

    def tax_calculation(self, product: Product):
        return product.price * Decimal(1.10)


"""_________________________Product Model Serializer____________"""


class ProductMSerializer(serializers.ModelSerializer):
    price_tax = serializers.SerializerMethodField(method_name='tax_calculation')

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'inventory', 'category', 'price_tax']
        read_only_fields = ['price_tax']

    # ________________Custom Methods_______________
    def tax_calculation(self, product: Product):
        return product.price * Decimal(1.10)

    # ______________________________________________

    # ____________For data Validation______________
    def validate(self, data):
        if data['title'] == "Saqib":
            return serializers.ValidationError("Saqib should not be used")
        return data

    # ______________________________________________
    # ________For Saving Objects___________________

    def create(self, validated_data):
        product = Product(**validated_data)
        product.is_available = True
        product.save()
        return product

    # ______________________________________________
    # ___________For Updating Objects_______________
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.category = validated_data.get('category')
        instance.price = validated_data.get('price')
        instance.inventory = validated_data.get('inventory')
        instance.save()
        return instance
    # _______________________________________________


""""--------------------Review Model Serializer----------------------"""


class ReviewModelSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['id', 'product', 'name', 'description']
        read_only_fields = ['product']

    def create(self, validated_data):
        product_id = self.context.get('product_id')
        return Review.objects.create(product_id=product_id, **validated_data)


""""--------------------CartItem Model Serializer----------------------"""


class CartItemSerializer(serializers.ModelSerializer):
    product_detail = ProductMSerializer(read_only=True, source='product')
    total_price = serializers.SerializerMethodField(method_name='get_total_price')

    class Meta:
        model = cart_item
        fields = ['id', 'product', 'product_detail', 'quantity', 'total_price']

    def get_total_price(self, cart: cart_item):
        return cart.quantity * cart.product.price

    def create(self, validated_data):
        cart_id = self.context.get('cart_id')
        product_id = self.validated_data.get('product')
        quantity = self.validated_data.get('quantity')
        print(cart_id, product_id, quantity)
        cart, created = cart_item.objects.get_or_create(cart_id=cart_id, product_id=product_id)
        cart.quantity += quantity
        return cart


""""--------------------Cart Model Serializer----------------------"""


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    cart = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')

    class Meta:
        model = Cart
        fields = ['id', 'cart', 'total_price']

    def get_total_price(self, carts: Cart):
        total = 0
        for item in carts.cart.all():
            total += item.quantity * item.product.price
        return total

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)
