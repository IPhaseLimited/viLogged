from django.conf.urls import patterns, include, url
from api.v1.appointments.views import AppointmentList, AppointmentDetail, AppointmentNestedDetail

urlpatterns = patterns('',
    url(r'^$', AppointmentList.as_view()),
    url(r'^(?P<uuid>\w+)/?$', AppointmentDetail.as_view()),
    url(r'^nested/(?P<uuid>\w+)/?$', AppointmentNestedDetail.as_view()),
)
