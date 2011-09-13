# -*- coding: utf-8 -*-
"""
Admin for Profile model
"""

from django.contrib import admin
from models import Registered, Participant, Winner


class RegisteredAdmin(admin.ModelAdmin):
	list_display =	("first_name",'first_surname','second_surname','email','home_phone','mobile_phone','ubigeo','document_code','register_date')



class ParticipantAdmin(admin.ModelAdmin):
	list_display =	("first_name",'first_surname','second_surname','email','home_phone','mobile_phone','ubigeo','document_code','get_user_code','register_date')
	#list_filter = ('get_user_code',)

class WinnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Registered, RegisteredAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Winner, WinnerAdmin)
