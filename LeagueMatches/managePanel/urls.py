from django.conf.urls import url
from . import views

app_name = 'manage'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login$',  views.auth, name='login'),
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
]
