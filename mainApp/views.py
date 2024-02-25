from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class OwnerRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ProductsAPIView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                description="Filter by Category ID",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="subCategory_id",
                in_=openapi.IN_QUERY,
                description="Filter by SubCategory ID",
                type=openapi.TYPE_INTEGER
            )
        ],
    )
    def get(self, request):
        products = Product.objects.all()
        if self.request.query_params.get("category_id"):
            products = products.filter(subCategory__category__id=self.request.query_params.get("category_id"))
        if self.request.query_params.get("subCategory_id"):
            products = products.filter(subCategory__id=self.request.query_params.get("subCategory_id"))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product_images = ProductImage.objects.filter(product=product)
        serializer = ProductImageSerializer(product_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
