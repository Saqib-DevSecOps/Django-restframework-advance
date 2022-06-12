from django_filters.rest_framework import FilterSet

from api.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'title':['icontains'],
            'price':['lt','gt']
        }