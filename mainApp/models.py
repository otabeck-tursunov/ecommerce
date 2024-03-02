from django.core.validators import *
from django.db import models
from coreApp.models import *


class Category(CoreModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', blank=True)

    def __str__(self):
        return self.name


class SubCategory(CoreModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Owner(CoreModel):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(CoreModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0)])
    amount = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(0)])
    guaranty = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    deliver = models.CharField(max_length=30, blank=True, null=True)
    battery = models.BooleanField(blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    avg_rating = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(CoreModel):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.product.name


class ProductProperty(CoreModel):
    name = models.CharField(max_length=255)
    context = models.CharField(max_length=1024)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

