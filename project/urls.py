# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Profile URLs
    (r'^manejatuvida/profile/', include('profile.urls')),
    
    # Contact URLs
    (r'^manejatuvida/contact/', include('contact.urls')),

    # Profile URLs
    (r'^manejatuvida/contest/', include('contest.urls')),
    
    # Home URLs
    (r'^manejatuvida/', include('main.urls')),
    
    # Home URLs
    (r'^manejatuvida/ubigeo/', include('ubigeo.urls')),

	#Facebook
    url(r'^manejatuvida/facebook_save/', 'facebook.views.save', name='facebook_save'),

	#Directos GA
	url(r'^manejatuvida/login.html',direct_to_template,{'template':'ga/login.html'},name='login.html'),
	url(r'^manejatuvida/compartir.html',direct_to_template,{'template':'ga/compartir.html'},name='compartir.html'),
	url(r'^manejatuvida/premios.html',direct_to_template,{'template':'ga/premios.html'},name='premios.html'),
	url(r'^manejatuvida/empaques.html',direct_to_template,{'template':'ga/empaques.html'},name='empaques.html'),
	url(r'^manejatuvida/comercial.html',direct_to_template,{'template':'ga/comercial.html'},name='comercial.html'),




)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$',
                serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
            url(r'^static/(?P<path>.*)$',
                serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
