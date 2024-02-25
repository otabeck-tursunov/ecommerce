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


class OwnerRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        if self.request.query_params.get('category_id'):
            products = products.filter(subCategory__category__id=self.request.query_params.get('category_id'))
        if self.request.query_params.get('subCategory_id'):
            products = products.filter(subCategory__id=self.request.query_params.get('subCategory_id'))
        return products


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
