from django.conf.urls import patterns, include, url
from api.v1.visitors.views import *

urlpatterns = patterns('',
    url(r'^$', VisitorsList.as_view()),
    #url(r'^(?P<pk>\w+)/?$', VisitorDetail.as_view()),
    url(r'^(?P<uuid>\w+)/?$', VisitorDetail.as_view()),
    url(r'^nested/?$', VisitorsNestedList.as_view()),
    url(r'^nested/(?P<uuid>\w+)/?$', VisitorNestedDetail.as_view()),
)