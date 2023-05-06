from products.models import Product
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import django_filters


 


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['price']
