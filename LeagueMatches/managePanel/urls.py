from django.conf.urls import url
from . import views

app_name = 'manage'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login$',  views.auth, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
]
