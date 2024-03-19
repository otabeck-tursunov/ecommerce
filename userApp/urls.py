from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserCreateAPIView.as_view()),
    path('all/', UserListAPIView.as_view()),
    path('update/', UserUpdateAPIView.as_view()),
    path('delete/', UserDestroyAPIView.as_view()),
    path('retrieve/', UserRetrieveAPIView.as_view()),

]
