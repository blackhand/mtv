# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns
from surlex.dj import surl as url

urlpatterns = patterns('ubigeo.views',
        url('^ubigeo/$', 'widget', name='widget'),
        ('^province/(?P<department>\d+)/$', 'get_provinces'),
)
