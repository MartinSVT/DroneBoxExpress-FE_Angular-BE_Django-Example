from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, RegisterSerializer, UserUpdateSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# sent get request with header key = Authorization and value = TOKEN "token value"
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserUpdateAPI(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'

    def update(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        instance = self.get_object()
        if instance.id == user.id:
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserDeleteAPI(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'

    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        instance = self.get_object()
        if instance.id == user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Error 401", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# post request with username, email, first_name, last_name, password, password2
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# post request to loginURL with body username and password
