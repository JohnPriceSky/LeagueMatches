from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import login, authenticate, logout
from .decorators import check_recaptcha
from django.conf import settings
from LeagueMatches.settings import RECAPTCHA_PRIVATE_KEY

import requests

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'auth.html')
    return render(request, 'panel.html')


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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'panel.html')
        else:
            return render(request, 'auth.html')
    # else:
    #     print("KASZANA")
    #     return render(request, 'auth.html')


def logout_view(request):
    logout(request)
    return render(request, 'auth.html')
