from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
