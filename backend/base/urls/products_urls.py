from django.urls import path

from base.views.product_views import get_products, get_product

urlpatterns = [
    path("products/", get_products, name="products"),
    path("products/<str:pk>/", get_product, name="product")
]
