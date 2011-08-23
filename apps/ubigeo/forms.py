# -*- coding: utf-8 -*-
"""
field and widget for Ubigeo Field
"""

from django.forms.widgets import MultiWidget, Select

from django.forms import ModelChoiceField

from models import Ubigeo


class UbigeoWidget(MultiWidget):
    """
    Widget to draw three selects for ubigeo, department, province and district
    """
    def __init__(self, *args, **kwargs):
        widgets = (
                Select(), Select()
                ,)


