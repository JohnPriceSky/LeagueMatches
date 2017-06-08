from django.shortcuts import render_to_response, redirect, render, get_list_or_404, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .decorators import check_recaptcha
from django.conf import settings
from LeagueMatches.settings import RECAPTCHA_PRIVATE_KEY
from game.models import Team, Player, Game, Serie, Stat, MapObjective, Event

import requests


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'auth.html')
    return render(request, 'manageHome.html')


#@check_recaptcha
def auth(request):
    # # Begin reCAPTCHA validation
    # recaptcha_response = request.POST.get('g-recaptcha-response')
    # data = {
    #     'secret': RECAPTCHA_PRIVATE_KEY,
    #     'response': recaptcha_response
    # }
    # r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    # result = r.json()
    # # End reCAPTCHA validation
    #
    # if result['success']:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/manage/')
        #else:
        #    return render(request, 'auth.html')
    # else:
    #     print("KASZANA")
    #     return render(request, 'auth.html')


def logout_view(request):
    logout(request)
    return redirect('/manage/')


def players(request):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    players = Player.objects.all()
    return render(request, 'managePlayers.html', {'players' : players})


def editPlayer(request, player_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'editPlayer.html', {'player' : player})


def updatePlayer(request, player_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        player = get_object_or_404(Player, id=player_id)
        player.name = request.POST.get('name')
        player.surname = request.POST.get('surname')
        player.nickname = request.POST.get('nickname')
        player.save()
    return redirect('/manage/player/' + str(player_id))


def addPlayer(request):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        nickname = request.POST.get('nickname')
        player = Player.objects.create(name=name,
                                       surname=surname,
                                       nickname=nickname,
                                       team=get_object_or_404(Team, id=5))
        player.save()
    return redirect('/manage/players')


def teams(request):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    teams = Team.objects.all()
    return render(request, 'manageTeams.html', {'teams' : teams})


def editTeam(request, team_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    team = get_object_or_404(Team, id=team_id)
    players = Player.objects.filter(team_id=team_id)
    freePlayers = Player.objects.filter(team_id=5)
    return render(request, 'editTeam.html', {'team' : team, 'players' : players, 'freePlayers' : freePlayers})


def addTeam(request):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        name = request.POST.get('name')
        team = Team.objects.create(name=name)
        team.save()
        id = team.id
        return redirect('/manage/team/' + str(id))
    return redirect('/manage/teams')


def addPlayerToTeam(request, team_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        player_id = request.POST.get('player')
        player = get_object_or_404(Player, id=player_id)
        player.team = get_object_or_404(Team, id=team_id)
        player.save()
    return redirect('/manage/team/' + str(team_id))


def disbandPlayer(request, team_id, player_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    player = get_object_or_404(Player, id=player_id)
    player.team = get_object_or_404(Team, id=5)
    player.save()
    return redirect('/manage/team/' + str(team_id))


def renameTeam(request, team_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        team = get_object_or_404(Team, id=team_id)
        team.name = request.POST.get('name')
        team.save()
    return redirect('/manage/team/' + str(team_id))


def removeTeam(request, team_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    players = Player.objects.filter(team_id=team_id)
    for p in players:
        p.team = get_object_or_404(Team, id=5)
        p.save()
    team = get_object_or_404(Team, id=team_id)
    team.delete()
    return redirect('/manage/teams')


def matches(request):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    games = Game.objects.all()
    teams = Team.objects.all()
    return render(request, 'manageMatches.html', {'games' : games, 'teams' : teams})


def editMatch(request, game_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    game = get_object_or_404(Game, id=game_id)
    stats = Stat.objects.filter(game_id=game_id)
    return render(request, 'editMatch.html', {'game' : game, 'stats' : stats})


def addMatch(request):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        date = request.POST.get('date')
        length = request.POST.get('length')
        team_a_id = request.POST.get('team_a')
        team_b_id = request.POST.get('team_b')
        winner_id = request.POST.get('winner')
        if(winner_id == 1):
            winner_id = team_a_id
        else:
            winner_id = team_b_id
        serie = get_object_or_404(Serie, id=2)
        match = Game.objects.create(date=date,
                                    length=length,
                                    teamA=get_object_or_404(Team, id=team_a_id),
                                    teamB=get_object_or_404(Team, id=team_b_id),
                                    winner=get_object_or_404(Team, id=winner_id),
                                    serie=serie)
        match.save()
        players = Player.objects.filter(team_id=team_a_id)
        for p in players:
            stat = Stat.objects.create(game=match,
                                       player=p)
        players = Player.objects.filter(team_id=team_b_id)
        for p in players:
            stat = Stat.objects.create(game=match,
                                       player=p)
    return redirect('/manage/matches')


def updateStat(request, stat_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    stat = get_object_or_404(Stat, id=stat_id)
    if request.method == 'POST':
        stat.kills = request.POST.get('kills')
        stat.deaths = request.POST.get('deaths')
        stat.assists = request.POST.get('assists')
        stat.save()
    return redirect('/manage/match/' + str(stat.game_id))


def editObjectives(request, stat_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    stat = get_object_or_404(Stat, id=stat_id)
    events = Event.objects.filter(stat_id=stat_id)
    mapObjectives = MapObjective.objects.all()
    return render(request, 'editObjectives.html', {'stat' : stat, 'events' : events, 'obj' : mapObjectives})


def addObjective(request, stat_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        obj_id = request.POST.get('objective')
        obj = get_object_or_404(MapObjective, id=obj_id)
        event = Event.objects.create(mapObjective=obj,
                                     stat=get_object_or_404(Stat, id=stat_id))
        event.save()
    return redirect('/manage/objectives/' + str(stat_id))


def removeObjective(request, stat_id, event_id):
    if not request.user.is_authenticated:
        return redirect('/manage/')
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('/manage/objectives/' + str(stat_id))