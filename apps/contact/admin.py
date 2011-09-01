# -*- coding: utf-8 -*-
"""
Admin for Contact model
"""

from django.contrib import admin
from models import Contact, RespondedContact, PendingContact


class ContactAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Profile
    """


admin.site.register(Contact, ContactAdmin)
admin.site.register(RespondedContact, ContactAdmin)
admin.site.register(PendingContact, ContactAdmin)
