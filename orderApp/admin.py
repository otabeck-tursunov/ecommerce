from django.contrib import admin
from .models import *

admin.site.register([Region, City, Cart, Order, OrderProduct])
