from django.shortcuts import render
from rest_framework.views import APIView,Response
from teams.models import Team
from django.forms.models import model_to_dict
from utils import (
    data_processing,
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError,
)


class TeamView(APIView):
    def post(self, request):
        team_data = request.data
        try:
            data_processing(team_data)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as error:
            return Response({"error": error.message}, status=400)

        team = Team.objects.create(**team_data)
        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list)
