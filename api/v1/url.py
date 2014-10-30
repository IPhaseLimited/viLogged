from django.conf.urls import patterns, include, url
from api.v1.views import *

urlpatterns = patterns('',
    url(r'^users$', UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^user/$', UserList.as_view()),
    url(r'^current-user/$', GetUserByToken.as_view()),
)