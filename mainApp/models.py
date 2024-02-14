from django.db import models
from coreApp.models import CoreModel


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
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(CoreModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    amount = models.PositiveSmallIntegerField(default=1)
    discount = models.PositiveSmallIntegerField(default=0)
    guaranty = models.CharField(max_length=30, blank=True, null=True)
    deliver = models.CharField(max_length=30, blank=True, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, blank=True, null=True)


class ProductImage(CoreModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.product.name


