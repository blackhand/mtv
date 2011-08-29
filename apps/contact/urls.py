# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns
from surlex.dj import surl as url

urlpatterns = patterns('contact.views',
        url('^send/', 'contact_send', name='contact_send'),
        ##url('^register/', 'profile_register', name='profile_register'),
)
