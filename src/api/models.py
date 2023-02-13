from uuid import uuid4

from core.settings import AUTH_USER_MODEL
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.product.title


class Order(models.Model):
    payment_choice = (
        ('p', 'pending'),
        ('c', 'complete'),
        ('f', 'failed')
    )
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(choices=payment_choice,max_length=20)
    customer = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.PROTECT)

    def __str__(self):
        return self.customer.username

