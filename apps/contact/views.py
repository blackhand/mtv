# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.mail import send_mail
from smtplib import SMTPException

from models import Contact

def send(request):
    if request.method == 'POST':
        contact = Contact.objects.create(
                          first_name = request.POST[""],
                          second_name = request.POST[""],
                          mail = request.POST[""],
                          comment = request.POST[""],
                          reply = request.POST[""],
                          responded = request.POST[""],
                          )
        contact.save()
    
