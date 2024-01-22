from django.shortcuts import get_object_or_404
from products.models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .cart import Cart
from .models import Order
from .serializers import CartAddSerializer, OrderSerializer


class CartView(APIView):
    def get(self, request):
        cart = Cart(request)
        return Response(
            {"data": list(cart.__iter__()),
            "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )


class CartAddView(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        srz_data = CartAddSerializer(data=request.POST)
        if srz_data.is_valid():
            cart.add(product=product, quantity=srz_data.validated_data["quantity"])
            return Response({"message": "Cart updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRemoveView(APIView):
    def delete(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return Response({"message": "Product removed"}, status=status.HTTP_202_ACCEPTED)


class OrderDetailView(APIView):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        if order.paid is False:
            srz_date = OrderSerializer(instance=order).data
            return Response(srz_date, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Your order has been paid"}, status=status.HTTP_200_OK)
