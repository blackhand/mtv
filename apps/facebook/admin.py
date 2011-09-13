
from django.contrib import admin

from models import FacebookUser


class FacebookUserAdmin(admin.ModelAdmin):
	list_display = ("name",'email','gender','created_date')



admin.site.register(FacebookUser,FacebookUserAdmin)
