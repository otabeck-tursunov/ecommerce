from rest_framework import serializers
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
