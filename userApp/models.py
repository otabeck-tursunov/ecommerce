import uuid

from django.db import models
from django.contrib.auth.models import User

from coreApp.models import CoreModel
from orderApp.models import City


class CustomUser(CoreModel):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
