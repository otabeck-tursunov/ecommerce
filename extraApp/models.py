from django.core.validators import MinValueValidator
from django.db import models
from mainApp.models import *


class Display(models.Model):
    surface = models.CharField(max_length=255, blank=True, null=True)
    touch_screen = models.BooleanField(default=False)
    frame_rate = models.PositiveSmallIntegerField(blank=True, null=True)
    matrix_type = models.CharField(max_length=255, blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    dioganal = models.FloatField(validators=[MinValueValidator(0.0), ], blank=True, null=True)

    product = models.OneToOneField(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Display: {self.product.name}'


class Processor(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    gen = models.PositiveSmallIntegerField(blank=True, null=True)
    core = models.PositiveSmallIntegerField(blank=True, null=True)
    thread = models.PositiveSmallIntegerField(blank=True, null=True)
    min_frequency = models.FloatField(blank=True, null=True)
    max_frequency = models.FloatField(blank=True, null=True)
    cache = models.PositiveSmallIntegerField(blank=True, null=True)
    video_card = models.CharField(max_length=255, blank=True, null=True)

    product = models.OneToOneField(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Processor: {self.model} | {self.product}'


class RAM(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    size = models.PositiveSmallIntegerField(blank=True, null=True)

    product = models.OneToOneField(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'RAM: {self.model} | {self.product.name}'


class VideoCard(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    size = models.PositiveSmallIntegerField(blank=True, null=True)

    product = models.OneToOneField(Product, on_delete=models.SET_NULL, blank=True, null=True)

    # def __str__(self):
    #     return f'VideoCard: {self.model} | {self.product.name}'


class Camera(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    pixel_size = models.PositiveSmallIntegerField(blank=True, null=True)

    product = models.OneToOneField(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Camera: {self.model} | {self.product.name}'
