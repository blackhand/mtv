# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.core.validators import email_re
from datetime import date

from captcha import CaptchasDotNet

from ubigeo.models import Ubigeo
from profile.models import Profile
from contest.models import Option

import urllib2
import urllib
from django.views.decorators.csrf import csrf_exempt 
import pdb

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
        birth_date = date(int(year), int(month), int(day))
    except:
        return HttpResponse('error')

    try:
        profile = Profile.objects.get(email=email)
        if profile.birth_date == birth_date:
            request.session['profile_id'] = profile.pk
            return HttpResponse('exist')
        else:
            return HttpResponse('error')

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

@csrf_exempt
def validate_form_captcha(request):
	
    code = request.POST.get('codigo')

    recaptcha_challenge_field = request.POST.get('recaptcha_challenge_field')
    recaptcha_response_field = request.POST.get('recaptcha_response_field') 



    #pdb.set_trace()

    recaptcha_values = 	{'privatekey' :	'6LcZB8gSAAAAAAHbaCnh-_V82fZ5fvJials2X3Ae',\
			'remoteip' : request.META['REMOTE_ADDR'] ,\
			'challenge' : recaptcha_challenge_field,\
			'response' :  recaptcha_response_field }

    urequest = urllib2.Request("http://www.google.com/recaptcha/api/verify",urllib.urlencode(recaptcha_values))
    try:
       response = urllib2.urlopen(urequest)
    except urllib2.URLError, e:
       return HttpResponse('error')

	
    response = response.read()
    is_accepted = response.split("\n")[0]

    print is_accepted

    try:
        profile = Profile.objects.get(pk=request.session['profile_id'])
        if is_accepted == "true":
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
            return HttpResponse('captcha_error')

    except Exception, e:
        return HttpResponse('error')


def validate_generic(request):
    code = request.GET.get('code')
    generic = code[0:2]
    generic_codes = {
            'MC': 1,
            'ME': 2,
            'LP': 2,
            'MF': 2,
            'MR': 1,
            'TR': 1,
            'UE': 2,
            'MJ': 1,
            'MK': 1,
            'ZE': 2,
            'UF': 2,
            'SL': 1,
            'RN': 2,
            'PA': 1,
            'PC': 1,
            'NW': 1,
            'PT': 1,
            'PZ': 1,
            'PK': 1,
            'YY': 1,
            'RA': 1,
            'PN': 1,
            'C4': 1,
            'C3': 1,
            'PM': 1,
            'YZ': 1,
            'MZ': 1,
            'NE': 1,
            'MW': 1,
            'MY': 1,
    }
    if generic in generic_codes:
        return HttpResponse(generic_codes[generic])
    else:
        return HttpResponse('notvalid')


def get_profile_name(request):
    profile = Profile.objects.get(pk=request.session['profile_id'])
    profile_name = profile.first_name + ' ' + profile.first_surname
    return HttpResponse(profile_name)


def facebook_send(request):
    return HttpResponse('pass')
