from django.conf.urls import patterns, include, url
from api.v1.core.views import *
from lib.utility import send_mail

urlpatterns = patterns('',

    url(r'^company-entrances/?$', CompanyEntranceNamesList.as_view()),
    url(r'^company-entrance/(?P<uuid>\w+)/$', CompanyEntranceNamesDetail.as_view()),
    url(r'^departments/?$', CompanyDepartmentsList.as_view()),
    url(r'^department/(?P<uuid>\w+)/?$', CompanyDepartmentsDetail.as_view()),
    url(r'^restricted-items/?$', RestrictedItemsList.as_view()),
    url(r'^restricted-items/(?P<uuid>\w+)/$', RestrictedItemsDetail.as_view()),
    url(r'^send-email/?$', SendEmail.as_view()),
    url(r'^vehicles/?$', VehicleList.as_view()),
    url(r'^vehicle/(?P<uuid>\w+)/?$', VehicleDetail.as_view()),
)