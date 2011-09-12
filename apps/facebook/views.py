from django.shortcuts import render_to_template
from models import FacebookUser

def save(request):

	fbid = request.POST.get("fbid")
	username = request.POST.get("username")
	gender = request.POST.get("gender")
	birthday = request.POST.get("birthday")
	email = request.POST.get("email")

	fb_user = FacebookUser()
	fb_user.facebook_id = fbid
	fb_user.username = username
	fb_user.email = email
	fb_user.gender = gender
	fb_user.birthday = birthday
	fb_user.save()

