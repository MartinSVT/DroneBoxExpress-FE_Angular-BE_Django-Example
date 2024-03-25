from django.db import models
from enum import Enum
from django.core.validators import MinValueValidator
from DroneBoxExpressBE.Core.mixins import EnumMixin
from DroneBoxExpressBE.StaffLogic.models import RoutesModel
from django.contrib.auth.models import User


class OrderStatus(EnumMixin, Enum):
    Scheduled = "Scheduled"
    Completed = "Completed"


class OrdersModel(models.Model):
    order_route = models.ForeignKey(
        to=RoutesModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=False,
        null=False
    )
    cost = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0.0)]
    )
    order_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    order_status = models.CharField(
        choices=OrderStatus.list_choices(),
        max_length=OrderStatus.max_len(),
        default="Scheduled",
        null=False,
        blank=False,
    )



