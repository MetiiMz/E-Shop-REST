from rest_framework import serializers
from products.models import Product
from .models import Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartAddSerializer(serializers.Serializer):
    """
    Serializer for adding a product to the cart with a specified quantity.
    """
    quantity = serializers.IntegerField()


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for showing order items with nested product details.
    """
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying order details including items.
    """
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
