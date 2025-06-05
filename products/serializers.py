from rest_framework import serializers
from .models import Product


class ProductListSerializers(serializers.ModelSerializer):
    """
    Serializer for listing product information.
    """
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializers(serializers.ModelSerializer):
    """
    Serializer for detailed product information.
    """
    class Meta:
        model = Product
        fields = '__all__'
