from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics as api_views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from DroneBoxExpressBE.StaffLogic.models import AirportModel, RoutesModel, NewsModel
from DroneBoxExpressBE.StaffLogic.serializers import AirportSerializer, RouteSerializer, NewsSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import json


# NEWS VIEWS
class NewsListView(api_views.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class NewsCreateView(api_views.CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class NewsUpdateDeleteView(api_views.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = NewsModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'pk'

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        instance = self.get_object()

        if instance.article_user == user:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        instance = self.get_object()

        if instance.article_user == user:
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        instance = self.get_object()

        if instance.article_user == user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Airports VIEWS
class AirportListView(api_views.ListCreateAPIView):
    queryset = AirportModel.objects.all()
    serializer_class = AirportSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AirportUpdateDeleteView(api_views.RetrieveUpdateDestroyAPIView):
    serializer_class = AirportSerializer
    queryset = AirportModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'


# Routes VIEWS
class RoutesListView(api_views.ListCreateAPIView):
    queryset = RoutesModel.objects.all()
    serializer_class = RouteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class RoutesUpdateDeleteView(api_views.RetrieveUpdateDestroyAPIView):
    serializer_class = RouteSerializer
    queryset = RoutesModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'
