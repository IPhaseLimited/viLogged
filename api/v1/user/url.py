from django.conf.urls import patterns, include, url
from api.v1.user.views import *

urlpatterns = patterns('',
    url(r'^(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^$', UserList.as_view()),
)