from django import forms
from DroneBoxExpressBE.CustomerLogic.models import OrdersModel


class OrdersAddForm(forms.ModelForm):
    class Meta:
        model = OrdersModel
        fields = ["order_route", 'weight', 'cost', 'order_user', 'order_status']