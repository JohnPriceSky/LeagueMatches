from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


def home(request):
    print(4544544544)
    if not request.user.is_authenticated:
        return render(request, 'auth.html')
    return render(request, 'udalosie.html')


# COS TU KOMBINOWALEM, ALE JESZCZE NIE DZIALA
def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'udalosie.html')
    else:
        return render(request, 'auth.html')


def logout_view(request):
    logout(request)
    return render(request, 'auth.html')
