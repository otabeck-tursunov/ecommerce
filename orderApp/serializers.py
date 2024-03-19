from rest_framework import serializers

from mainApp.serializers import ProductCascadeSerializer
from .models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class RegionCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityCascadeSerializer(serializers.ModelSerializer):
    region = RegionCascadeSerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'region')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'amount', 'product', 'created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'phone_number', 'total_price', 'payment', 'city', 'address', 'floor')


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'
