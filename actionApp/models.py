from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from coreApp.models import CoreModel
from mainApp.models import Product
from userApp.models import CustomUser


class Rating(CoreModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.product.name} - {self.rating}"


class Liked(CoreModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"
