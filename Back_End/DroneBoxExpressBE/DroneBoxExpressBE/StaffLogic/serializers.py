from rest_framework import serializers
from DroneBoxExpressBE.StaffLogic.models import AirportModel, RoutesModel, NewsModel


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportModel
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutesModel
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = "__all__"
