from django.conf.urls import url
from . import views

app_name = 'manage'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login$', views.auth, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^players$', views.players, name='players'),
    url(r'^player/(?P<player_id>[0-9]+)$', views.editPlayer, name='editPlayer'),
    url(r'^UpdatePlayer/(?P<player_id>[0-9]+)$', views.updatePlayer, name='updatePlayer'),
    url(r'^AddPlayer$', views.addPlayer, name='addPlayer'),
    url(r'^teams$', views.teams, name='teams'),
    url(r'^team/(?P<team_id>[0-9]+)$', views.editTeam, name='editTeam'),
    url(r'^AddTeam$', views.addTeam, name='addTeam'),
    url(r'^AddPlayerToTeam/(?P<team_id>[0-9]+)$', views.addPlayerToTeam, name='addPlayerToTeam'),
    url(r'^AddPlayerToTeam/(?P<team_id>[0-9]+)/(?P<player_id>[0-9]+)$', views.disbandPlayer, name='disband'),
    url(r'^RenameTeam/(?P<team_id>[0-9]+)$', views.renameTeam, name='renameTeam'),
    url(r'^RemoveTeam/(?P<team_id>[0-9]+)$', views.removeTeam, name='removeTeam'),
    url(r'^matches$', views.matches, name='matches'),
    url(r'^match/(?P<game_id>[0-9]+)$', views.editMatch, name='editMatch'),
    url(r'^AddMatch$', views.addMatch, name='addMatch'),
    url(r'^UpdateStat/(?P<stat_id>[0-9]+)$', views.updateStat, name='updateStat'),
    url(r'^objectives/(?P<stat_id>[0-9]+)$', views.editObjectives, name='editObjectives'),
    url(r'^AddObjective/(?P<stat_id>[0-9]+)$', views.addObjective, name='addObjective'),
    url(r'^RemoveObjective/(?P<stat_id>[0-9]+)/(?P<event_id>[0-9]+)$', views.removeObjective, name='removeObjective'),
    url(r'^series$', views.series, name='series'),
    url(r'^AddSerie$', views.addSerie, name='addSerie'),
    url(r'^serie/(?P<serie_id>[0-9]+)$', views.editSerie, name='editSerie'),
]
