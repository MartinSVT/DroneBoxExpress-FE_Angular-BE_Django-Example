from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# News Article Model
class NewsModel(models.Model):
    article_title = models.CharField(blank=False, null=False, max_length=30)
    article_content = models.TextField(blank=False, null=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    article_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )


# Airport Model (to be implemented)
class AirportModel(models.Model):
    airport_name = models.CharField(blank=False, null=False, max_length=50)
    longitude = models.FloatField(blank=False, null=False)
    latitude = models.FloatField(blank=False, null=False)


# Route Model
class RoutesModel(models.Model):
    origin_airport = models.ForeignKey(
        to=AirportModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='Route_Origin_Airport'
    )
    destination_airport = models.ForeignKey(
        to=AirportModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='Route_Destination_Airport'
    )
    cost_per_kg = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=False,
        null=False
    )


