# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

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

	#Facebook
    url(r'^facebook_save/', 'facebook.views.save', name='facebook_save'),

	#Directos GA
	url(r'^login.html',direct_to_template,{'template':'ga/login.html'},name='login.html'),
	url(r'^compartir.html',direct_to_template,{'template':'ga/compartir.html'},name='compartir.html'),
	url(r'^premios.html',direct_to_template,{'template':'ga/premios.html'},name='premios.html'),
	url(r'^empaques.html',direct_to_template,{'template':'ga/empaques.html'},name='empaques.html'),
	url(r'^comercial.html',direct_to_template,{'template':'ga/comercial.html'},name='comercial.html'),




)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$',
                serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
            url(r'^static/(?P<path>.*)$',
                serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
