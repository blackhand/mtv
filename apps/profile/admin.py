# -*- coding: utf-8 -*-
"""
Admin for Profile model
"""

from django.contrib import admin
from models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Profile
    """


admin.site.register(Profile, ProfileAdmin)
