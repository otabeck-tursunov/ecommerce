from rest_framework import serializers
from .models import *


class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Display
        fields = ('surface', 'touch_screen', 'frame_rate', 'matrix_type', 'resolution', 'dioganal')


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = (
            'model', 'brand', 'family', 'gen', 'core',
            'thread', 'min_frequency', 'max_frequency', 'cache', 'video_card'
        )


class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = ('model', 'type', 'brand', 'size',)


class VideoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCard
        fields = ('model', 'type', 'brand', 'size')


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('model', 'type', 'brand', 'pixel_size')


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('amount', 'deadline')
