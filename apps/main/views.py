# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.core.validators import email_re
from datetime import date

from captcha import CaptchasDotNet

from ubigeo.models import Ubigeo
from profile.models import Profile
from contest.models import Option

def not_implemented(request):
    return HttpResponse('NOT IMPLEMENTED')

def captcha(request):
    captcha = CaptchasDotNet(
            client   = 'tribalperu',
            secret   = 'ZLydlgOUioIEeLb4p2dQYyyVGFYKRimzTwxcUSfT',
            alphabet = 'abcdefghkmnopqrstuvwxyz',
            letters  = 7,
            width    = 215,
            height   = 60,)
    return render(request, 'main/_captcha.html', locals())


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
        return HttpResponse('error')

    try:
        birthday = date(int(year), int(month), int(day))
    except:
        return HttpResponse('error')

    try:
        profile = Profile.objects.get(email=email)
        request.session['profile_id'] = profile.pk
        return HttpResponse('exist')

    except Profile.DoesNotExist:
        return HttpResponse('not-exist')


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
        profile = Profile.objects.create(
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
        request.session['profile_id'] = profile.pk
        return HttpResponse('success')

    except:
        return HttpResponse('error')


def validate_form_captcha(request):
    code = request.GET.get('codigo')
    random = request.GET.get('random')
    password = request.GET.get('password')

    captcha = CaptchasDotNet(
            client   = 'tribalperu',
            secret   = 'ZLydlgOUioIEeLb4p2dQYyyVGFYKRimzTwxcUSfT',
            alphabet = 'abcdefghkmnopqrstuvwxyz',
            letters  = 7,)

    try:
        profile = Profile.objects.get(pk=request.session['profile_id'])
        if captcha.validate(random) and captcha.verify(password):
            try:
                option = Option.objects.get(product_code = code)
                return HttpResponse('exist')
            except:
                pass

            Option.objects.create(
                    participant = profile,
                    product_code = code)
            return HttpResponse('success')
        else:
            raise Exception
    except Exception, e:
        return HttpResponse('error')

