# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import render, redirect
from forms import LoginForm, ProfileForm

from models import Profile


def profile_login(request):
    """
    we 'login' every user with email and birthdate selected
    if user dont exist, we pass to profile_register
    """
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            try:
                profile = Profile.objects.get(email=login_form.cleaned_data['email'])
                return redirect('profile_enter_code')
            except Profile.DoesNotExist:
                return redirect('profile_register')
    else:
        login_form = LoginForm()
    return render(request, 'profile/profile_login.html', {
        'login_form': login_form, 
        })


def profile_register(request):
    """
    Register new profile, if success, login and go to enter code page
    else, error and try again
    """
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save()
            login(request, profile.user)
            return redirect('profile_enter_code')

    profile_form = ProfileForm(request.POST)
    return render(request, 'profile/profile_register.html', {
        'profile_form': profile_form, 
        })
