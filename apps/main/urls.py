# -*- coding: utf-8 -*-

from django.conf.urls.defaults import url, patterns
#from surlex.dj import surl as url

urlpatterns = patterns('main.views',
        url('^$', 'main_homepage', name='main_homepage')
)
