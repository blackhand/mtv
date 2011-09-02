# -*- coding: utf-8 -*-
"""
Admin for Ubigeo model
"""

from django.contrib import admin
from models import Ubigeo
from forms import UbigeoForm

class UbigeoAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Ubigeo
    """
    form = UbigeoForm


admin.site.register(Ubigeo, UbigeoAdmin)
