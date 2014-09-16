from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from viLogged.views import *
from django.contrib.auth.models import User
from core.models import UserProfile, Vehicle, Visitors, VisitorsLocation, VisitorGroup, Appointments, MessageQueue,\
    AppLicenseDuration, DocumentManagement

from django.contrib import admin


urlpatterns = patterns('',
    #url(r'^$', HomePageView.as_view()),

    url(r'^$', StaffsListView.as_view()),
    url(r'^add/$', StaffFormView.as_view()),
    url(r'^detail/(?P<pk>\d+)(/*)$', 'staff.views.user_profile_view'),
    url(r'^profile/$', 'staff.views.user_profile_view'),
    url(r'^approve-appointment/(?P<pk>\d+)/(?P<uuid>\w+)$', 'staff.views.user_profile_view'),
)