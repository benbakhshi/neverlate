from django.conf.urls import patterns, include, url
from apps.sms.views import EventDetailView, EventListView, CreateEventView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # url(r'^$', 'reminders.views.home', name='home'),
                       # url(r'^reminders/', include('reminders.foo.urls')),
                       url(r'^event/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event'),
                       url(r'^create-event/$', CreateEventView.as_view(), name='createevent'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
