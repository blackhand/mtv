# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns
from surlex.dj import surl as url

urlpatterns = patterns('ubigeo.views',
        url(r'^get_ubigeo/<ubigeo_id:#>/', 'get_ubigeo', name='get_ubigeo'),
        url(r'^ubigeo/$', 'widget', name='widget'),
        ('^province/(?P<department>\d+)/$', 'get_provinces'),
)
