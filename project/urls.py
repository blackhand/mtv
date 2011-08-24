# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Profile URLs
    (r'^profile/', include('profile.urls')),

    # Home URLs
    (r'', include('home.urls')),
)
