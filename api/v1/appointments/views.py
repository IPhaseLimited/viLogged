from rest_framework import serializers, generics, mixins
from core.models import Appointments, RestrictedItems, Vehicle
from api.v1.core.serializers import CompanyEntranceNamesSerializer
from api.permissions import *
from api.serializer import *
from api.v1.visitors.views import VisitorSerializer
from api.v1.user.views import UserNestedSerializer, UserProfileNestedSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    visitor_id = UUIDRelatedField(many=False)
    entrance_id = UUIDRelatedField(many=False, blank=True)

    class Meta:
        model = Appointments
        fields = ('visitor_id', 'representing', 'purpose', 'appointment_date', 'visit_start_time', 'visit_end_time',
                  'host_id', 'escort_required', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id',
                  'uuid')


class AppointmentNestedSerializer(serializers.ModelSerializer):
    visitor_id = VisitorSerializer(many=False)
    host_id = UserNestedSerializer(many=False)
    entrance_id = CompanyEntranceNamesSerializer(many=False)

    class Meta:
        model = Appointments
        fields = ('representing', 'purpose', 'appointment_date', 'visit_start_time', 'visit_end_time', 'host_id',
                  'escort_required', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid',
                  'visitor_id')


class AppointmentList(generics.ListAPIView, mixins.CreateModelMixin):

    model = Appointments
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id', 'escort_required',
                     'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid', 'visitor_id')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentNestedList(generics.ListAPIView, mixins.CreateModelMixin):

    model = Appointments
    serializer_class = AppointmentNestedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id__id', 'escort_required',
                     'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid', 'visitor_id__uuid')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView, mixins.CreateModelMixin):
    model = Appointments
    serializer_class = AppointmentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id', 'escort_required',
                     'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid', 'visitor_id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentNestedDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                              generics.GenericAPIView, mixins.CreateModelMixin):
    model = Appointments
    serializer_class = AppointmentNestedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id__id', 'escort_required',
                     'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid', 'visitor_id__uuid')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)