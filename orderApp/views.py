from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class RegionListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]

    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CitiesAPIView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="region_id",
                in_=openapi.IN_QUERY,
                description="Filter by Region ID",
                type=openapi.TYPE_INTEGER,
            )
        ]
    )
    def get(self, request):
        cities = City.objects.all()
        if request.query_params.get('region_id'):
            cities = City.objects.filter(region__id=request.query_params.get('region_id'))
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

