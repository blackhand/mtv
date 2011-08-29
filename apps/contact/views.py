# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import get_or_create

from models import Contact

##def contact(request):
    
def contact_send(request):
    if request.method == 'POST':
        contact, created = Contact.objects.get_or_create(
                                   first_name = request.POST["first_name"],
                                   second_name = request.POST["second_name"],
                                   email = request.POST["email"],
                                   comment = request.POST["comment"],
                                   )
        contact.save()
    return render(request, 'main/main_homepage.html')
