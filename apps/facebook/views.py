from django.shortcuts import render_to_response
from models import FacebookUser
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse

@csrf_exempt
def save(request):

	fbid = request.POST.get("id")
	name = request.POST.get("name")
	link = request.POST.get("link")
	gender = request.POST.get("gender")
	birthday = request.POST.get("birthday")
	email = request.POST.get("email")

	d = datetime.strptime(birthday, '%m/%d/%Y')

	fb_user = FacebookUser()
	fb_user.facebook_id = fbid
	fb_user.name = name
	fb_user.link = link
	fb_user.email = email
	fb_user.gender = gender
	fb_user.birthday = d.strftime('%Y-%m-%d')
	fb_user.save()

	return HttpResponse("true")
