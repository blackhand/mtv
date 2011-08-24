# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from profile.forms import ProfileForm

urlpatterns = patterns('',
    # Profile and Registration URLs
    (r'^accounts/', include('profile.urls'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    # Home URLs
    (r'', include('home.urls')),
)
