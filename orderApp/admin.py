from django.contrib import admin
from .models import *

admin.site.register([Region, City, Liked, Cart, Order, OrderProduct])
