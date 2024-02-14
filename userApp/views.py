from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import *
from rest_framework.response import Response

from .models import CustomUser
from .serializers import *


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return get_object_or_404(CustomUser, user=self.request.user)


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(CustomUser, user=self.request.user)


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(CustomUser, user=self.request.user)

    def delete(self, request, *args, **kwargs):
        custom_user = self.get_object()
        user = get_object_or_404(User, id=self.request.user.id)
        user.delete()
        custom_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
