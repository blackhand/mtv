# -*- coding: utf-8 -*-

from django.conf.urls.defaults import url, patterns
#from surlex.dj import surl as url

urlpatterns = patterns('home.views',
        url('^$', 'homepage', name='homepage')
)
