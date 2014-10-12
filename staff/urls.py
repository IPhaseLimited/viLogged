from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from staff.views import *
from django.contrib.auth.models import User
from core.models import UserProfile, Vehicle, Visitors, VisitorsLocation, VisitorGroup, Appointments, MessageQueue,\
    AppLicenseDuration, DocumentManagement

from django.contrib import admin


urlpatterns = patterns('',
    #url(r'^$', HomePageView.as_view()),

    url(r'^$', StaffsListView.as_view(), name='staff_home'),
    url(r'^add/$', StaffFormView.as_view(), name='staff_form'),
    url(r'^edit/(?P<pk>\d+)$', StaffFormView.as_view(), name='staff_edit_pk'),
    url(r'^edit/$', StaffFormView.as_view(), name='staff_edit'),
    url(r'^detail/(?P<pk>\d+)(/*)$', 'staff.views.user_profile_view', name='staff_detail'),
    url(r'^profile/$', 'staff.views.user_profile_view', name='staff_profile'),
    url(r'^approve-appointment/(?P<pk>\d+)/(?P<uuid>\w+)$', 'staff.views.user_profile_view'),
)