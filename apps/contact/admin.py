# -*- coding: utf-8 -*-
"""
Admin for Contact model
"""

from django.contrib import admin
from models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Profile
    """


admin.site.register(Contact, ContactAdmin)
