# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def not_implemented(request):
    return HttpResponse('NOT IMPLEMENTED')

def main_homepage(request):
    return render(request, 'main/main_homepage.html')
