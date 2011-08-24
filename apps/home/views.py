# -*- coding: utf-8 -*-

from django.http import HttpResponse

def not_implemented(request):
    return HttpResponse('NOT IMPLEMENTED')
