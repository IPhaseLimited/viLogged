from django.conf.urls import patterns, include, url
from appointments.views import *

urlpatterns = patterns('',
    #url(r'^$', 'appointments.views.get_all_appointments'),
    url(r'^$', AppointmentsListView.as_view()),
    url(r'^add-appointment$', AppointmentsFormView.as_view()),
    url(r'^approved/$', AppointmentsListView.as_view()),
    url(r'^in-progress/$', AppointmentsListView.as_view()),
    url(r'^pending/$', AppointmentsListView.as_view()),
    url(r'^inactive/$', AppointmentsListView.as_view()),
)