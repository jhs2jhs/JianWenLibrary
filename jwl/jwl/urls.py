from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url

from views import hello, current_datetime, welcome, welcome_request

from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
    url(r'^$', welcome),
    url(r'^welcome/request$', welcome_request),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^book/', include('books.urls')),
    
)
