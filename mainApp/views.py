from django.shortcuts import render
from rest_framework import generics, status
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


class ProductListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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
