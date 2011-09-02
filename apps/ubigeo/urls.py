# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns
from surlex.dj import surl as url

urlpatterns = patterns('ubigeo.views',
        url('^ubigeo/$', 'widget', name='widget'),
        url(r'^province/(?P<department_id>\d+)/$', 'get_provinces', name='get_provinces'),
)
