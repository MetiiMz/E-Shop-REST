from django.shortcuts import get_object_or_404
from products.models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .cart import Cart
from .models import Order, OrderItem
from .serializers import CartAddSerializer, OrderSerializer


class CartView(APIView):
    """
    Get cart from session and return its content with total price
    """
    def get(self, request):
        cart = Cart(request)
        return Response(
            {"data": list(cart.__iter__()),
            "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )


class CartAddView(APIView):
    """
    Add a product with given quantity to the cart (requires authentication)
    """
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        srz_data = CartAddSerializer(data=request.data)
        if srz_data.is_valid():
            cart.add(product=product, quantity=srz_data.validated_data["quantity"])
            return Response({"message": "Cart updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRemoveView(APIView):
    """
    Remove the product from the cart (requires authentication)
    """
    def delete(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return Response({"message": "Product removed"}, status=status.HTTP_202_ACCEPTED)


class OrderListView(ListAPIView):
    """
    List all orders for authenticated user (admin sees all)
    """
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)


class OrderCreateView(APIView):
    """
    Create a new order from current cart content and clear the cart
    """
    def post(self, request):
        cart = Cart(request)
        if not cart:
            return Response({"message": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.create(user=request.user)
        for item in cart:
            product_data = item['product']
            product_instance = Product.objects.get(id=product_data['id'])
            OrderItem.objects.create(
                order=order,
                product=product_instance,
                price=item['price'],
                quantity=item['quantity'],
            )
        cart.clear()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
