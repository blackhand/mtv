"""
Forms and validation code for user profile.

"""
from django import forms
from profile.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
