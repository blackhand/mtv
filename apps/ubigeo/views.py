# -*- coding: utf-8 -*-

from django.shortcuts import render
from ubigeo.forms import UbigeoForm, UbigeoWidget
from django.utils import simplejson
from django.http import HttpResponse
from django.core import serializers
from ubigeo.models import Ubigeo


def widget(request):
    ubigeowidget = UbigeoForm()
    return render(request, 'ubigeo/ubigeo.html',{
        'ubigeowidget':ubigeowidget,
        })


def get_provinces(request, department):
    provinces = UbigeoWidget().get_province(department)
    arr_j = {}
    for province in provinces:
        arr_j[province[0]]=province[1]
    return HttpResponse(simplejson.dumps(arr_j),mimetype='application/json')


def get_districts(request, province):
    return HttpResponse(simplejson.dumps(province),mimetype='application/json')


def get_ubigeo(request,ubigeo_id):
    if request.is_ajax():
        ubigeo = Ubigeo.objects.filter(parent = ubigeo_id)
        data = serializers.serialize('json', ubigeo)
        return HttpResponse(data,'application/javascript') 


