from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

from django.contrib import admin 

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'login.views.start'), 
    url(r'^login/$', 'login.views.userlogin'),
    url(r'^logout/$', 'login.views.logout_view'),
    url(r'^welcome/$', 'login.views.welcome'),
    url(r'^welcome/blood/$','login.views.blood'),
    url(r'^welcome/blood/create/$','login.views.createblood'),	
    url(r'^welcome/profile/$','login.views.myprofile'),
    url(r'^welcome/events/$','login.views.events'),
    url(r'^welcome/createevent/$','login.views.createevent'),
    url(r'^welcome/events/eventdetail/(?P<variable>\d+)/$','login.views.eventdetail'),
    url(r'^signup/$','login.views.createuser'),
    
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
  
    url(r'^admin/', include(admin.site.urls)),
)
