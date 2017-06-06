from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render_to_response('login.html')

# COS TU KOMBINOWALEM, ALE JESZCZE NIE DZIALA
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            render_to_response('udalosie.html')
        else:
            print "disabled account"
    else:
       print "invalid login"


def logout_view(request):
    logout(request)