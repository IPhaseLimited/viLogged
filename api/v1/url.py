from django.conf.urls import patterns, include, url
from api.v1.user.views import UserList, GetUserByToken, UserNestedList
from api.v1.visitors.views import VisitorsNestedList, VisitorsLocationDetail, VisitorsLocationList, VisitorsGroupDetail, VisitorsGroupList
from api.v1.appointments.views import AppointmentNestedList
from api.v1.core.views import *

urlpatterns = patterns('',
    url(r'^appointments/nested/?$', AppointmentNestedList.as_view()),
    url(r'^company-entrance/?$', CompanyEntranceNamesList.as_view()),
    url(r'^company-entrance/(?P<uuid>\w+)/?$', CompanyEntranceNamesDetail.as_view()),
    url(r'^company-departments/?$', CompanyDepartmentsList.as_view()),
    url(r'^company-departments/(?P<uuid>\w+)/?$', CompanyDepartmentsDetail.as_view()),
    url(r'^current-user/?$', GetUserByToken.as_view()),
    url(r'^restricted-items/?$', RestrictedItemsList.as_view()),
    url(r'^restricted-items/(?P<uuid>\w+)/?$', RestrictedItemsDetail.as_view()),
    url(r'^send-email/?$', SendEmail.as_view()),
    url(r'^vehicles/?$', VehicleList.as_view()),
    url(r'^vehicle/(?P<uuid>\w+)/?$', VehicleDetail.as_view()),
    url(r'^visitors/nested/?$', VisitorsNestedList.as_view()),
    url(r'^users/?$', UserList.as_view()),
    url(r'^users/nested/?$', UserNestedList.as_view()),

    url(r'^appointments/?', include('api.v1.appointments.url')),
    url(r'^core/?', include('api.v1.core.url')),
    url(r'^company-departments/?', include('api.v1.core.url')),
    url(r'^report/?', include('api.v1.reports.url')),
    url(r'^visitors/?', include('api.v1.visitors.url')),
    url(r'^visitors-group/?$', VisitorsGroupList.as_view()),
    url(r'^visitors-group/(?P<uuid>\w+)/?$', VisitorsGroupDetail.as_view()),
    url(r'^visitors-location/?$', VisitorsLocationList.as_view()),
    url(r'^visitors-location/(?P<uuid>\w+)/?$', VisitorsLocationDetail.as_view()),
    url(r'^user/?', include('api.v1.user.url')),



)