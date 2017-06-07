from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'manage'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login$',  views.auth, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
]
