from rest_framework import serializers
from .models import *


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'product', 'rating', 'created_at', 'updated_at')


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked
        fields = ('id', 'product', 'created_at', 'updated_at')