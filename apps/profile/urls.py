# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns
from surlex.dj import surl as url

urlpatterns = patterns('profile.views',
        url('^login/', 'profile_login', name='profile_login'),
        url('^register/', 'profile_register', name='profile_register'),
)
