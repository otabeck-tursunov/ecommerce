from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404

from .models import *
from orderApp.models import City
from orderApp.serializers import *


class CustomUserSerializer(serializers.ModelSerializer):
    city = CityCascadeSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address',
                  'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address',
                  'created_at', 'updated_at')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', None),
            first_name=validated_data.get('first_name', ""),
            last_name=validated_data.get('last_name', "")
        )

        customUser = CustomUser.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', None),
            first_name=validated_data.get('first_name', ""),
            last_name=validated_data.get('last_name', ""),
            phone_number=validated_data.get('phone_number', None),
            city=validated_data.get('city', None),
            address=validated_data.get('address', ""),
            user=user
        )
        return customUser

    def update(self, instance, validated_data):
        user = User.objects.get(username=instance.username)
        user.username = validated_data.get('username', instance.username)
        user.password = validated_data.get('password', instance.password)
        user.email = validated_data.get('email', instance.email)
        user.first_name = validated_data.get('first_name', instance.first_name)
        user.last_name = validated_data.get('last_name', instance.last_name)
        user.save()

        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.username)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        city_data = validated_data.pop('city', None)
        if isinstance(city_data, int):
            instance.city = City.objects.get(id=city_data)
        else:
            instance.city = city_data

        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

