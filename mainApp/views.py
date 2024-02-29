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
        data = []
        for product in products:
            product_data = ProductSerializer(product).data
            images = ProductImage.objects.filter(product=product)
            img_main = None
            img_sub = []
            for image in images:
                if not img_main:
                    img_main = image.image.url
                else:
                    img_sub.append(image.image.url)
            product_data['img_main'] = img_main
            product_data['img_sub'] = img_sub

            # barcha propertylar
            properties = ProductProperty.objects.filter(product=product)
            property_serializer = ProductPropertySerializer(properties, many=True)
            product_data['properties'] = property_serializer.data

            data.append(product_data)
        return Response(data, status=status.HTTP_200_OK)


class ProductAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            product_serializer = ProductSerializer(product)
            images = ProductImage.objects.filter(product=product)
            img_main = None
            img_sub = []
            for image in images:
                if not img_main:
                    img_main = image.image.url
                else:
                    img_sub.append(image.image.url)

            properties = ProductProperty.objects.filter(product=product)
            property_serializer = ProductPropertySerializer(properties, many=True)

            data = {
                'product': product_serializer.data,
                'img_main': img_main,
                'img_sub': img_sub,
                'properties': property_serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class ProductImageAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product_images = ProductImage.objects.filter(product=product)
        serializer = ProductImageSerializer(product_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
