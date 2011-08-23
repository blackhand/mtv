# -*- coding: utf-8 -*-

from forms import ProfileForm
from django.shortcuts import render, redirect

def register(request):
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/accounts/register/')
    return render(request, 'registration/registration_form.html', {
        'form': profile_form}
        )
