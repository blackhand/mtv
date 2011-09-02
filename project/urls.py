# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    # Profile URLs
    (r'^profile/', include('profile.urls')),
    
    # Contact URLs
    (r'^contact/', include('contact.urls')),

    # Profile URLs
    (r'^contest/', include('contest.urls')),
    
    # Home URLs
    (r'', include('main.urls')),
    
    # Home URLs
    (r'^ubigeo/', include('ubigeo.urls')),

)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$',
                serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
            url(r'^static/(?P<path>.*)$',
                serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
