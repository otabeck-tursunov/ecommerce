from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class RatingCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        ratings = Rating.objects.filter(user=request.user)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            product = get_object_or_404(Product, id=serializer.data.get('product'))
            product_rating = Rating.objects.filter(product=product).values_list('rating', flat=True)
            if product_rating:
                r = sum(product_rating) / len(product_rating)
            else:
                r = None
            product.avg_rating = r
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LikedAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        likeds = Liked.objects.filter(user=CustomUser.objects.get(user=request.user))
        serializer = LikedSerializer(likeds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LikedSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=CustomUser.objects.get(user=request.user))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response({"succes": False, "messages": "This product already liked"},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnLikedAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, product_id):
        liked = get_object_or_404(Liked, product=Product.objects.get(id=product_id))
        if liked.user == CustomUser.objects.get(user=request.user):
            liked.delete()
            return Response({
                "succes": True,
                "message": "Product unliked successfully!"
            })
        return Response({
            "succes": False,
            "message": "The product does not belong to the user!"
        })
