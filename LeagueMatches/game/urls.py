from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^schedule/$', views.show_schedule, name="schedule"),
    url(r'^teams/$', views.show_teams, name="teams"),
    url(r'^games/(?P<serie_id>[0-9]+)/$', views.show_games, name="games"),
]