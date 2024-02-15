from rest_framework import serializers

from userApp.models import Rating
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')


class CategoryCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategoryCascadeSerializer()

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category', 'created_at', 'updated_at')


class SubCategoryCascadeSerializer(serializers.ModelSerializer):
    category = CategoryCascadeSerializer()

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category')


class ProductSerializer(serializers.ModelSerializer):
    subCategory = SubCategoryCascadeSerializer()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'amount', 'discount', 'guaranty', 'deliver', 'owner', 'subCategory',
            'created_at', 'updated_at')


class ProductCascadeSerializer(serializers.ModelSerializer):
    subCategory = SubCategoryCascadeSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'subCategory')


class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductCascadeSerializer()

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'product', 'created_at', 'updated_at')
