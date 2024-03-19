from django.urls import path
from .views import *

urlpatterns = [
    path('rating/', RatingCreateAPIView.as_view()),
    path('liked/', LikedAPIView.as_view()),
    path('liked/<int:product_id>/', UnLikedAPIView.as_view()),
]
