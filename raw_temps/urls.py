from django.conf.urls import patterns, include, url
from django.conf import settings
from raw_temps.views import *



urlpatterns = patterns('',
    url(r'^modal-staff-form$', staff_form),
)