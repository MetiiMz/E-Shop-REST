from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
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
        page_number = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('limit', 9)
        paginator = Paginator(products, page_size)
        srz_date = ProductListSerializers(instance=paginator.page(page_number), many=True)
        return Response(srz_date.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get(self, request, product_slug):
        products = get_object_or_404(Product, slug=product_slug)
        srz_date = ProductDetailSerializers(instance=products)
        return Response(srz_date.data, status=status.HTTP_200_OK)
