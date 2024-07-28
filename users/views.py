from django.shortcuts import render, redirect
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse



def login_user(request):

    if request.method == "POST":

        form = LoginUserForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse("main:index"))
            else:
                messages.error(request, "Your account is disabled or unknown")
    else:

        form = LoginUserForm()

    return render(request, "users/login.html", {"form" : form})
    
def register_user(request):
    if request.method == "POST":

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            return HttpResponseRedirect(reverse('users:login'))
    else:

        form = RegisterUserForm()
    return render(request, "users/register.html", {"form" : form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:index"))

