# -*- coding: utf-8 -*-
"""
Settings for admin site
"""

from settings import *

INSTALLED_APPS = BASE_INSTALLED_APPS + (
    'grappelli',
    'django.contrib.admin',
)

ROOT_URLCONF = 'project.admin_urls'
