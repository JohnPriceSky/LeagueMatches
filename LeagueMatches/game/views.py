from django.shortcuts import render_to_response, get_list_or_404
from django.http import Http404
from .models import Serie, Game, Team, Player


def home(request):
    return render_to_response('home.html')


def show_schedule(request):
    series = Serie.objects.all()
    return render_to_response('schedule.html', {'series': series})


def show_games(request, serie_id):
    games = get_list_or_404(Game, serie_id=serie_id)
    return render_to_response('games.html', {'games': games})


def show_teams(request):
    teams = Team.objects.all()
    return render_to_response('teams.html', {'teams': teams})


def show_players(request, team_id):
    players = get_list_or_404(Player, team_id=team_id)
    return render_to_response('players.html', {'players': players})


def about(request):
    return render_to_response('about.html')


def contact(request):
    return render_to_response('contact.html')