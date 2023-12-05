from django import forms

from .models import City, Team, Player, Stadium

#City Forms ------------------------------------------------------------------------------
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "city_name",
        ]
        widgets = {
            "city_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

class UpdateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "city_name",
        ]
        widgets = {
            "city_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

#Team Forms ---------------------------------------------------------------------------
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "team_name",
            "venue",
            "players",
            "director",
        ]
        widgets = {
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "venue": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

class UpdateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "team_name",
            "venue",
            "players",
            "director",
        ]
        widgets = {
            "team_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "venue": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "players": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "director": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

#Player Forms -------------------------------------------------------------------------
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "team",
            "player_name",
            "number",
            "position",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "player_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "number": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "position": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

class UpdatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "team",
            "player_name",
            "number",
            "position",
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "player_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "number": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"}),
            "position": forms.TextInput(attrs={"type":"form-select", "class":"form-control"})
        }

#Stadium Forms -----------------------------------------------------------------------------
class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "team",
            "city",
            "stadium_name",
            "capacity"
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "city": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "capacity": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"})
        }

class UpdateStadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = [
            "team",
            "city",
            "stadium_name",
            "capacity"
        ]
        widgets = {
            "team": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "city": forms.Select(attrs={"type":"form-select", "class":"form-control"}),
            "stadium_name": forms.TextInput(attrs={"type":"form-select", "class":"form-control"}),
            "capacity": forms.NumberInput(attrs={"type":"form-select", "class":"form-control"})
        }