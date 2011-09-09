# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.core.validators import email_re
from datetime import date

from ubigeo.models import Ubigeo
from profile.models import Profile

def not_implemented(request):
    return HttpResponse('NOT IMPLEMENTED')


def main_homepage(request):
    days = range(1,31)
    months = {
            1: 'Enero', 
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'
            }
    years = range(1900, 1999)
    departments = Ubigeo.objects.departments()
    return render(request, 'main/main_homepage.html', locals())


def validate_form1(request):
    email = request.GET.get('email')
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    if (not email) or (not email_re.match(email)):
        return HttpResponse('email-error')
    try:
        birthday = date(int(year), int(month), int(day))
    except:
        return HttpResponse('date-error')

    try:
        profile = Profile.objects.get(email=email)
    except Profile.DoesNotExist:
        return HttpResponse('not-exist')

    return HttpResponse('exist')


def validate_form2(request):
    email = request.GET.get('email')
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    names = request.GET.get('names')
    last_name1 = request.GET.get('last_name1')
    last_name2 = request.GET.get('last_name2')
    ubigeo = request.GET.get('ubigeo')
    address = request.GET.get('address')
    phone = request.GET.get('phone')
    mobile = request.GET.get('mobile')
    doc_number = request.GET.get('doc_number')

    if (not email) or (not email_re.match(email)):
        return HttpResponse('error')
    try:
        birthday = date(int(year), int(month), int(day))
    except:
        return HttpResponse('error')

    if (not names) or (not last_name1) or (not last_name2) or (not ubigeo) or (not address) or (not phone) or (not mobile) or (not doc_number):
        return HttpResponse('error')

    try:
        ubigeo = Ubigeo.objects.get(pk=int(ubigeo))
        Profile.objects.create(
            first_name = names,
            first_surname = last_name1,
            second_surname = last_name2,
            email = email,
            birth_date = birthday,
            ubigeo = ubigeo,
            address = address, 
            home_phone = phone,
            mobile_phone = mobile,
            document_code = doc_number,)
    except:
        return HttpResponse('error')

    return HttpResponse('sucess')


def validate_form_captcha(request):
   return HttpResponse('.form-clave-correcta')
