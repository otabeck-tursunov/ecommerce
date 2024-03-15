from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

from mainApp.models import *
from coreApp.models import *


class Region(CoreModel):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name


class City(CoreModel):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Liked(CoreModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"


class Cart(CoreModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"


class Order(CoreModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    total_price = models.FloatField(default=0)
    payment = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    floor = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}: {self.created_at}"


class OrderProduct(CoreModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"
