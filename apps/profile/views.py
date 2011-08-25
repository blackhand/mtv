# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from forms import LoginForm, ProfileForm

from home.views import not_implemented


def profile_login(request):
    """
    we 'login' every user with email and birthdate selected
    if user dont exist, we pass to profile_register
    """
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user, created = User.get_or_create(username = request.POST["email"],password = request.POST["birth_date"])
            if created:
                return redirect('profile_register')
            else:
                return redirect('main_homepage')
    login_form = LoginForm()
    return render(request, 'profile/profile_login.html', {
        'login_form': login_form, 
        })

def profile_register(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return not_implemented(request)
    profile_form = ProfileForm(request.POST)
    return render('profile/profile_register.html', {
        'profile_form': profile_form, 
        })
