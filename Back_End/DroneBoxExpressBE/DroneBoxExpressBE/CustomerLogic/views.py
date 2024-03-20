from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics as api_views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from DroneBoxExpressBE.CustomerLogic.models import OrdersModel
from DroneBoxExpressBE.CustomerLogic.serializers import OrdersSerializer


class OrdersListCreateView(api_views.ListCreateAPIView):
    queryset = OrdersModel.objects.all()
    serializer_class = OrdersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class OrdersUpdateDeleteView(api_views.RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = OrdersModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
