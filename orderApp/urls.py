from django.urls import path
from .views import *

urlpatterns = [
    path('regions/', RegionListAPIView.as_view()),
    path('cities/', CitiesAPIView.as_view()),

    path('cart/', CartAPIView.as_view()),
    path('cart/<int:pk>/', CartRetrieveUpdateDeleteView.as_view()),

    path('', OrdersAPIView.as_view()),
]