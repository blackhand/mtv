# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import get_or_create, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from home.views import not_implemented


def profile_login(request):
    """
    we 'login' every user with email and birthdate selected
    if user dont exist, we pass to profile_register
    """
    if request.method = 'POST':
        profile_form = LoginForm(request.POST)
        if profile_form.is_valid():
            user, created = User.get_or_create(username = request.POST["email"],password = request.POST["birth_date"])
            if created:
				return HttpResponseRedirect(reverse('profile_register',))
			else:
				return render_to_response('main/homepage.html', context_instance=RequestContext(request))
    profile_form = LoginForm()
    return render_to_response('profile/profile_login.html', { 'profile_form': profile_form, }, context_instance=RequestContext(request))

def profile_register(request):
    return not_implemented(request)
