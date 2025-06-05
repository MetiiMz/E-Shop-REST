from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products'),
    path('detail/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]
