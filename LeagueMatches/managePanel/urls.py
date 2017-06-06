from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'manage'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', auth_views.login, {'template_name': '/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
