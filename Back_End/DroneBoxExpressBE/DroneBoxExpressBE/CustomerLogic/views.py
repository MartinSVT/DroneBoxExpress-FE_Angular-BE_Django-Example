from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics as api_views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from DroneBoxExpressBE.CustomerLogic.models import OrdersModel
from DroneBoxExpressBE.CustomerLogic.serializers import OrdersSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class OrdersListCreateView(api_views.ListCreateAPIView):
    queryset = OrdersModel.objects.all()
    serializer_class = OrdersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data['order_user'] == user:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        queryset = self.filter_queryset(self.get_queryset())

        if user.is_staff:
            mydata = queryset
        else:
            mydata = queryset.filter(order_user=user)

        serializer = self.get_serializer(mydata, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrdersUpdateDeleteView(api_views.RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    queryset = OrdersModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        instance = self.get_object()

        if user.is_staff:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            if instance.order_user == user:
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            else:
                return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        instance = self.get_object()

        if user.is_staff:
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            if instance.order_user == user:
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

        if user.is_staff:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            if instance.order_user == user:
                self.perform_destroy(instance)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
