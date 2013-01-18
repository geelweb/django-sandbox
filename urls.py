from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sandbox.views.home', name='home'),
    url(r'^quickpoll-app$', 'sandbox.views.quickpoll', name='quickpoll'),
    url(r'^twitter-bootstrap-form$', 'sandbox.views.twitter_bootstrap_form', name='twitter_bootstrap_form'),
    # url(r'^sandbox/', include('sandbox.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^contact$', 'geelweb.django.contactform.views.contact', name='contact'),
    url(r'^quickpoll/', include('geelweb.django.quickpoll.urls')),
)
