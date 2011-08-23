# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from profile.forms import ProfileForm

from registration.views import activate
from registration.views import register

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    # (r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$',
        register,
        {'backend': 'registration.backends.simple.SimpleBackend','form_class':ProfileForm},
        name='registration_register'),
    (r'^accounts/form/', 'profile.views.register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
