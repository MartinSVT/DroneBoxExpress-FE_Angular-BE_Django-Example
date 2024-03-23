from django.contrib import admin
from DroneBoxExpressBE.CustomerLogic.models import OrdersModel
from DroneBoxExpressBE.CustomerLogic.forms import OrdersAddForm


class OrdersModelAdmin(admin.ModelAdmin):
    list_display = ["order_route", 'weight', 'cost', 'order_user', 'order_status']
    form = OrdersAddForm
    ordering = ["order_route"]
    list_filter = ["order_route"]
    list_display_links = ["order_route", 'weight', 'cost', 'order_user', 'order_status']
    search_fields = ["order_route", 'weight', 'cost', 'order_user', 'order_status']


admin.site.register(OrdersModel, OrdersModelAdmin)
