from django.contrib import admin

from src.api.models import Product, Category, Cart, Review, cart_item, Order, OrderItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(cart_item)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
