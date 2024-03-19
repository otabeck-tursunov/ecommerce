from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *

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


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user__id=self.request.user.id)


class OrdersAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        carts = Cart.objects.filter(user=request.user)
        if carts.count() == 0:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save(user=request.user)
            order = Order.objects.get(id=serializer.data['id'])
            for cart in carts:
                OrderProduct.objects.create(
                    user=request.user,
                    product=cart.product,
                    amount=cart.amount,
                    order=order
                )
            carts.delete()
            orderProducts = OrderProduct.objects.filter(user=request.user, order=order)
            orderProducts_serializer = OrderProductSerializer(orderProducts, many=True)
            total_price = 0
            for orderProduct in orderProducts:
                total_price += orderProduct.product.price * orderProduct.amount
                print(total_price)
            order.total_price = total_price
            order.save()
            serializer = OrderSerializer(order)
            response = {
                'message': 'Successfully created order',
                'order': serializer.data,
                'order_products': orderProducts_serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
