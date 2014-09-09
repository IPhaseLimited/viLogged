from django.conf.urls import patterns, include, url
from appointments.views import *

urlpatterns = patterns('',
    url(r'^$', 'appointments.views.get_all_appointments'),
)