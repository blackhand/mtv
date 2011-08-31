# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns
from surlex.dj import surl as url

urlpatterns = patterns('contest.views',
        url('^winners/', 'show_winners', name='show_winners'),
)
