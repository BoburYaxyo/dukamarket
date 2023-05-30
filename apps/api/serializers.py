from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from shopping.models import Product, Review
from django.utils.translation import gettext_lazy as _


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
