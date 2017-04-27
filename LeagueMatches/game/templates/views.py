from django.shortcuts import render, render_to_response
from .models import Serie, Game, Team


def home(request):
    return render_to_response('home.html')

def show_schedule(request):
    series = Serie.objects.all()
    return render_to_response('schedule.html', {'series': series})

def show_games(request, serie_id):
    try:
        games = Game.objects.filter(serie_id=serie_id)
    except Team.DoesNotExist:
        raise Http404("Team does not exist")
    
    return render_to_response('games.html', {'games': games})

def show_teams(request):
    teams = Team.objects.all();
    return render_to_response('teams.html', {'teams': teams})