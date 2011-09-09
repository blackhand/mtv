# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns
from surlex.dj import surl as url

urlpatterns = patterns('main.views',
        url('^$', 'main_homepage', name='main_homepage'),
        url('validate_form1$', 'validate_form1', name='validate_form1'),
        url('validate_form2$', 'validate_form2', name='validate_form2'),
        url('validate_form_captcha$', 'validate_form1', name='validate_form_captcha'),
)
