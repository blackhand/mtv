# -*- coding: utf-8 -*-
"""
Admin for Profile model
"""

from django.contrib import admin
from models import Registered, Participant, Winner


class RegisteredAdmin(admin.ModelAdmin):
    pass


class ParticipantAdmin(admin.ModelAdmin):
    pass


class WinnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Registered, RegisteredAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Winner, WinnerAdmin)
