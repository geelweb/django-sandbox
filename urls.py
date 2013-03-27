from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sandbox.views',
    url(r'^$', 'home', name='home'),
    url(r'^quickpoll-app$', 'quickpoll', name='quickpoll'),
    url(r'^twitter-bootstrap-form$', 'twitter_bootstrap_form', name='twitter_bootstrap_form'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^quickpoll/', include('geelweb.django.quickpoll.urls')),
)

urlpatterns += patterns('geelweb.django.contactform.views',
    url(r'^contact$', 'contact', name='contact'),
)
