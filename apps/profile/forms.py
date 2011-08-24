# -*- coding: utf-8 -*-

"""
Forms and validation code for user profile.

"""
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from profile.models import Profile


class LoginForm(forms.Form):
    """
    This is not a real login form, but is the form for "login"
    users in this site
    """
    email = forms.EmailField()
    birth_date = forms.DateField(widget=SelectDateWidget())


class ProfileForm(forms.ModelForm):
    """
    Profile form, nothing fancy here
    """
    exclude = ('user',)
    class Meta:
        model = Profile

