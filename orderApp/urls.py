from django.urls import path
from .views import *

urlpatterns = [
    path('regions/', RegionListAPIView.as_view()),
    path('cities/', CitiesAPIView.as_view()),


]