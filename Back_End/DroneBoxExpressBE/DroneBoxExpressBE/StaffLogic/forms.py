from django import forms
from DroneBoxExpressBE.StaffLogic.models import AirportModel, RoutesModel, NewsModel


class AirportAddForm(forms.ModelForm):
    class Meta:
        model = AirportModel
        fields = ["airport_name", 'longitude', 'latitude']


class RoutesAddForm(forms.ModelForm):
    class Meta:
        model = RoutesModel
        fields = ["origin_airport", 'destination_airport', 'cost_per_kg']


class NewsAddForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ["article_title", 'article_content', 'article_user']
