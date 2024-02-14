from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer