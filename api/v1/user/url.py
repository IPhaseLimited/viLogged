from django.conf.urls import patterns, include, url
from api.v1.user.views import *

urlpatterns = patterns('',
    url(r'^(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^import/?$', UserImport.as_view()),
    url(r'^$', UserList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/?$', UserProfileDetail.as_view()),
    url(r'^profile/nested/(?P<pk>[0-9]+)/?$', UserProfileNestedDetail.as_view()),
    url(r'^profile/?$', UserProfileList.as_view()),
    url(r'^profile/nested/?$', UserProfileNestedList.as_view()),
    url(r'^set/', include('djoser.urls')),
)