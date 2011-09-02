# -*- coding: utf-8 -*-

from django.shortcuts import render
from ubigeo.forms import UbigeoForm, UbigeoWidget
from django.utils import simplejson


def widget(request):
    ubigeowidget = UbigeoForm()
    return render(request, 'ubigeo/ubigeo.html',{
        'ubigeowidget':ubigeowidget,
        })


def get_provinces(request, department_id):
    provinces = UbigeoWidget.get_province(department_id)
    print provinces
    return HttpResponse(simplejson.dumps(provinces),mimetype='application/json')

def get_districts(request):
    department = request.GET["department"]
