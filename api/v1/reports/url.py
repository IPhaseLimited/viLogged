from django.conf.urls import patterns, include, url
from api.v1.visitors.views import *

urlpatterns = patterns('',
    url(r'^', VisitorsList.as_view()),
)