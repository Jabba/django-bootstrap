from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( '',
    url( r'^$',           'landing.views.index',     name = 'index' ),
    url( r'^about/$',     'landing.views.about',     name = 'about' ),
    url( r'^signup/$',    'landing.views.signup',    name = 'signup' ),
    url( r'^dashboard/$', 'landing.views.dashboard', name = 'dashboard' ),
    url( r'^admin/',      include( admin.site.urls ) ),
)

# Django URLs
urlpatterns += patterns( 'django.contrib.auth.views',
    url( r'^login/$',  'login',  { 'template_name' : 'login.html', }, name = 'login' ),
    url( r'^logout/$', 'logout', { 'next_page' : '/' },               name = 'logout' ),
)
