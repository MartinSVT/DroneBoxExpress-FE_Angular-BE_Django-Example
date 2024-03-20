from rest_framework import serializers
from DroneBoxExpressBE.CustomerLogic.models import OrdersModel


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        fields = "__all__"
