from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, UserUpdateAPI, UserDeleteAPI

urlpatterns = [
  path("get-details", UserDetailAPI.as_view()),
  path('register', RegisterUserAPIView.as_view()),
  path('update/<int:pk>/', UserUpdateAPI.as_view()),
  path('delete/<int:pk>/', UserDeleteAPI.as_view())
]