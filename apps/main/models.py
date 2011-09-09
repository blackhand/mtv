# -*- coding: utf-8 -*-

from django import forms
from ubigeo.forms import UbigeoField

class LoginForm(forms.Form):
    email = forms.EmailField()
    ubigeo = UbigeoField()

