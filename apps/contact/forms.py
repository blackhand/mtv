# -*- coding: utf-8 -*-

"""
Forms and validation code for user profile.

"""
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form, nothing fancy here
    """
    class Meta:
        model = Contact
