from django.contrib import admin

# Register your models here.
from api.models import Category, Product, Review, Cart, cart_item

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(cart_item)