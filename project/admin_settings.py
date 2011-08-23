# -*- coding: utf-8 -*-
"""
Settings for admin site
"""

from settings import *

INSTALLED_APPS = BASE_INSTALLED_APPS + (
    'grappelli',
    'django.contrib.admin',
    #apps
    'ubigeo',
    'profile',
    'contest',
)


GRAPPELLI_ADMIN_TITLE = 'CMS - MANEJA TU VIDA CON NOSOTRAS'
ROOT_URLCONF = 'admin_urls'
SITE_ID = 1
