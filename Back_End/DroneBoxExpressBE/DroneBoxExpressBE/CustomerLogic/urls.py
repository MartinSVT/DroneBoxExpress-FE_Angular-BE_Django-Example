from django.urls import path
from .views import OrdersListCreateView, OrdersUpdateDeleteView


urlpatterns = [
    path('orders/', OrdersListCreateView.as_view()),
    path('orders/<int:pk>/', OrdersUpdateDeleteView.as_view()),
]
