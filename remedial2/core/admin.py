from django.contrib import admin
from .models import City, Team, Player, Stadium
from .forms import CityForm, TeamForm, PlayerForm, StadiumForm

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    form = CityForm

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    form = TeamForm

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    form = StadiumForm

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    form = PlayerForm

# Register your models here.
