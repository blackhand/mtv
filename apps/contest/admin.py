# -*- coding: utf-8 -*-
"""
Admin for Profile model
"""

from django.contrib import admin
from models import Product, Option, Draw


admin.site.register(Product)
admin.site.register(Option)
admin.site.register(Draw)

