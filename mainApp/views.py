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


class SubCategoriesAPIView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='category_id',
                in_=openapi.IN_QUERY,
                description="Filter by Category ID",
                type=openapi.TYPE_INTEGER,
            )
        ]
    )
    def get(self, request):
        subCategories = SubCategory.objects.all()
        if request.query_params.get('category_id'):
            subCategories = subCategories.filter(category__id=request.query_params.get('category_id'))
        serializers = SubCategorySerializer(subCategories, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class SubCategoryRetrieveAPIView(APIView):
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
        data = []
        for product in products:
            product_data = ProductSerializer(product).data
            images = ProductImage.objects.filter(product=product)
            image_data = ProductImageSerializer(images, many=True).data
            product_data['images'] = image_data
            data.append(product_data)
        return Response(data, status=status.HTTP_200_OK)


class ProductAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product_serializer = ProductSerializer(product)
        images = ProductImage.objects.filter(product=product)
        image_serializer = ProductImageSerializer(images, many=True)
        data = {
            'product': product_serializer.data,
            'images': image_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

class ProductImageAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product_images = ProductImage.objects.filter(product=product)
        serializer = ProductImageSerializer(product_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
