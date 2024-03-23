from django.urls import path
from DroneBoxExpressBE.StaffLogic.views import NewsListView, NewsCreateView, NewsUpdateDeleteView
from DroneBoxExpressBE.StaffLogic.views import AirportListView, AirportUpdateDeleteView
from DroneBoxExpressBE.StaffLogic.views import RoutesListView, RoutesUpdateDeleteView

urlpatterns = [
    path('news/', NewsListView.as_view()),
    path('addNews/', NewsCreateView.as_view()),
    path('news/<int:pk>/', NewsUpdateDeleteView.as_view()),
    path('airports/', AirportListView.as_view()),
    path('airports/<int:pk>/', AirportUpdateDeleteView.as_view()),
    path('routes/', RoutesListView.as_view()),
    path('routes/<int:pk>/', RoutesUpdateDeleteView.as_view()),
]
