# -*- coding: utf-8 -*-

from django.shortcuts import render

from contact.models import Contact
from contact.forms import ContactForm

    
def contact_send(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact, created = Contact.objects.get_or_create(
                                       first_name = request.POST["first_name"],
                                       second_name = request.POST["second_name"],
                                       email = request.POST["email"],
                                       comment = request.POST["comment"],
                                       )
            contact.save()
    return render(request, 'contact/contact.html', {'contact_form':contact_form},)
