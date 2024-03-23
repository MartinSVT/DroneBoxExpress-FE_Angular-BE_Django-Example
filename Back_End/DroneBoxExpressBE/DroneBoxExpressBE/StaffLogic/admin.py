from django.contrib import admin
from DroneBoxExpressBE.StaffLogic.models import AirportModel, RoutesModel, NewsModel
from DroneBoxExpressBE.StaffLogic.forms import AirportAddForm, RoutesAddForm, NewsAddForm


class AirportModelAdmin(admin.ModelAdmin):
    list_display = ["airport_name", 'longitude', 'latitude']
    form = AirportAddForm
    ordering = ["airport_name"]
    list_filter = ["airport_name"]
    list_display_links = ["airport_name", 'longitude', 'latitude']
    search_fields = ["airport_name", 'longitude', 'latitude']


class RoutesModelAdmin(admin.ModelAdmin):
    list_display = ["origin_airport", 'destination_airport', 'cost_per_kg']
    form = RoutesAddForm
    ordering = ["origin_airport"]
    list_filter = ["origin_airport"]
    list_display_links = ["origin_airport", 'destination_airport', 'cost_per_kg']
    search_fields = ["origin_airport", 'destination_airport', 'cost_per_kg']


class NewsModelAdmin(admin.ModelAdmin):
    list_display = ["article_title", 'article_content', 'article_user']
    form = NewsAddForm
    ordering = ["article_title"]
    list_filter = ["article_title"]
    list_display_links = ["article_title", 'article_content', 'article_user']
    search_fields = ["article_title", 'article_content', 'article_user']


admin.site.register(AirportModel, AirportModelAdmin)
admin.site.register(RoutesModel, RoutesModelAdmin)
admin.site.register(NewsModel, NewsModelAdmin)
