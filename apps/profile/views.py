# -*- coding: utf-8 -*-

from django.contrib.auth import login
from home.views import not_implemented


def profile_login(request):
    """
    we 'login' every user with email and birthdate selected
    if user dont exist, we pass to profile_register
    """
    return not_implemented(request)

def profile_register(request):
    return not_implemented(request)
