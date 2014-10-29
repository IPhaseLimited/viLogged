from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from viLogged.views import *
from django.contrib.auth.models import User
from core.models import UserProfile, Vehicle, Visitors, VisitorsLocation, VisitorGroup, Appointments, MessageQueue,\
    AppLicenseDuration, DocumentManagement

from django.contrib import admin
admin.autodiscover()

from rest_framework import viewsets, routers, serializers, generics


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User


class UserProfileViewSet(viewsets.ModelViewSet):
    model = UserProfile


class VehicleViewSet(viewsets.ModelViewSet):
    model = Vehicle


class VisitorsViewSet(viewsets.ModelViewSet):
    model = Visitors
    filter_fields = ('visitors_phone', 'visitors_email', 'visitors_pass_code')


class VisitorsLocationViewSet(viewsets.ModelViewSet):
    model = VisitorsLocation


class VisitorGroupViewSet(viewsets.ModelViewSet):
    model = VisitorGroup


class AppointmentsViewSet(viewsets.ModelViewSet):
    model = Appointments


class MessageQueueViewSet(viewsets.ModelViewSet):
    model = MessageQueue


class AppLicenseDurationViewSet(viewsets.ModelViewSet):
    model = AppLicenseDuration


class DocumentManagementViewSet(viewsets.ModelViewSet):
    model = DocumentManagement
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users-profile', UserProfileViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'visitors', VisitorsViewSet)
router.register(r'visitors-location', VisitorsLocationViewSet)
router.register(r'visitor-group', VisitorGroupViewSet)
router.register(r'appointments', AppointmentsViewSet)
router.register(r'messages', MessageQueueViewSet)
router.register(r'app-license-duration', AppLicenseDurationViewSet)
router.register(r'document-management', DocumentManagementViewSet)

urlpatterns = patterns('',
    #url(r'^$', HomePageView.as_view()),
    url(r'^$', 'viLogged.views.home'),
    url(r'^appointments/', include('appointments.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^visitors/', VisitorsListView.as_view()),
    #url(r'^add-visitor/', 'viLogged.views.add_visitor'),
    url(r'^add-visitor/', VisitorsFormView.as_view()),
    url(r'^login(/*)$', login, name="login"),
    url(r'^logout(/*)$', logout, name="logout"),
    url(r'^staff/', include('staff.urls')),
    url(r'^system-settings/$', VisitorsFormView.as_view()),
    url(r'^reports/$', Reports.as_view()),
    url(r'^documents/$', VisitorsFormView.as_view()),
    url(r'^email/$', 'viLogged.views.send_email'),
    url(r'^sms/$', 'viLogged.views.sms'),
    url(r'^load-image/$', 'viLogged.views.load_bar_code'),
    url(r'^label/$', 'viLogged.views.label'),
    url(r'^api/', include('api.url')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)