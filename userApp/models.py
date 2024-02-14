from django.db import models
from django.contrib.auth.models import User

from coreApp.models import CoreModel
from orderApp.models import *


class CustomUser(CoreModel):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Rating(CoreModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.product.name} - {self.rating}"