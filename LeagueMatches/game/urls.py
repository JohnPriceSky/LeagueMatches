from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^schedule/$', views.show_schedule, name="schedule"),
    url(r'^teams/$', views.show_teams, name="teams"),
    url(r'^games/(?P<serie_id>[0-9]+)/$', views.show_games, name="games"),
    url(r'^players/(?P<team_id>[0-9]+)/$', views.show_players, name="players"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^sign_in/$', views.sign_in, name="sign_in"),
    url(r'^stat/$', views.stat, name="stat"),
    url(r'^stat2/(?P<player_id>[0-9]+)/$', views.stat2, name="stat2"),

    #registration
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
]
