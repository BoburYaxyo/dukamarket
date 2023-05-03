from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR Password does not exist")

    context = {'page': page}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            user = form.save(commit=False)
            user.username = username.lower()
            user.email = email
            user.password1 = password1
            user.password2 = password2
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('home')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'form': form}

    return render(request, 'login.html', context)


@login_required(login_url='login')
def checkout(request):

    context = {}
    return render(request, 'checkout.html', context)


def errorim(request):
    return render(request, '404.html')
