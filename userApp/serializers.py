from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from orderApp.models import City


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'city', 'address')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        customUser = CustomUser.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            city=validated_data['city'],
            address=validated_data['address'],
            user=user
        )
        return customUser

    def update(self, instance, validated_data):
        user = User.objects.filter(email=instance.email).first()
        user.username = validated_data['username']
        user.set_password(validated_data['password'])
        user.email = validated_data['email']
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()

        instance.username = validated_data['username']
        instance.password = validated_data['password']
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.phone_number = validated_data['phone_number']
        instance.city = City.objects.get(id=validated_data['city'])
        instance.address = validated_data['address']
        instance.save()
        return instance

    def delete(self, instance):
        user = User.objects.filter(email=instance.email).first()
        user.delete()
        instance.delete()
        return instance
