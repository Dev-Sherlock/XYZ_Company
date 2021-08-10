import django_filters as filters
from .models import *
class ProductFilter(filters.FilterSet):
    class Meta:
        model=Product
        fields=['category']


