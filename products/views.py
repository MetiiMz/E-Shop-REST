from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategoryListSerializers, ProductListSerializers, ProductDetailSerializers


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        srz_date = CategoryListSerializers(instance=categories, many=True)
        return Response(srz_date.data, status=status.HTTP_200_OK)


class ProductsListView(APIView):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        if category_slug:
            # To filter the category
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        srz_date = ProductListSerializers(instance=products, many=True)
        return Response(srz_date.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get(self, request, product_slug):
        products = get_object_or_404(Product, slug=product_slug)
        srz_date = ProductDetailSerializers(instance=products)
        return Response(srz_date.data, status=status.HTTP_200_OK)
