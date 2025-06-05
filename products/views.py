from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductListSerializers, ProductDetailSerializers


class ProductsListView(ListAPIView):
    """
    API view to retrieve the list of all available products.
    """
    permission_classes = [AllowAny]
    serializer_class = ProductListSerializers
    queryset = Product.objects.all()


class ProductDetailView(RetrieveAPIView):
    """
    API view to retrieve detailed information of a single product by slug.
    """
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    lookup_field = 'slug'
    lookup_url_kwarg = 'product_slug'
