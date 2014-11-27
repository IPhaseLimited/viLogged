from rest_framework import serializers, generics, mixins
from core.models import Appointments, RestrictedItems, Vehicle, CompanyEntranceNames
from api.v1.core.serializers import CompanyEntranceNamesSerializer, VehicleSerializer, RestrictedItemsSerializer
from api.permissions import *
from api.serializer import *
from api.v1.visitors.views import VisitorSerializer
from api.v1.user.views import UserNestedSerializer, UserProfileNestedSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    visitor_id = UUIDRelatedField(many=False)
    entrance_id = UUIDRelatedField(many=False)
    class Meta:
        model = Appointments
        fields = ('visitor_id', 'representing', 'purpose', 'appointment_date', 'visit_start_time', 'visit_end_time',
                  'host_id', 'escort_required', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id',
                  'uuid', 'label_code')


class AppointmentNestedSerializer(serializers.ModelSerializer):
    visitor_id = VisitorSerializer(many=False)
    host_id = UserNestedSerializer(many=False)
    entrance_id = CompanyEntranceNamesSerializer(many=False)
    vehicle = VehicleSerializer(many=False)
    restricted_items = RestrictedItemsSerializer(many=True)

    class Meta:
        model = Appointments
        fields = ('representing', 'purpose', 'appointment_date', 'visit_start_time', 'visit_end_time', 'host_id',
                  'escort_required', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid',
                  'visitor_id', 'vehicle', 'restricted_items', 'label_code')


class AppointmentList(generics.ListAPIView, mixins.CreateModelMixin):

    model = Appointments
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id', 'escort_required',
                     'label_code', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid',
                     'visitor_id')

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        queryset = Appointments.objects.all()

        uuid = self.request.QUERY_PARAMS.get('uuid', None)
        visitor_id__uuid = self.request.QUERY_PARAMS.get('visitor_id__uuid', None)
        host_id__id = self.request.QUERY_PARAMS.get('host_id__id', None)
        is_approved = self.request.QUERY_PARAMS.get('is_approved', None)
        is_expired = self.request.QUERY_PARAMS.get('is_expired', None)
        label_code = self.request.QUERY_PARAMS.get('label_code', None)

        if uuid is not None:
            queryset = queryset.filter(uuid=uuid)
        if visitor_id__uuid is not None:
            queryset = queryset.filter(visitor_id__uuid=visitor_id__uuid)
        if host_id__id is not None:
            queryset = queryset.filter(host_id__id=host_id__id)
        if is_approved is not None:
            queryset = queryset.filter(is_approved=is_approved)
        if is_expired is not None:
            queryset = queryset.filter(is_expired=is_expired)
        if label_code is not None:
            queryset = queryset.filter(label_code=label_code)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentNestedList(generics.ListAPIView, mixins.CreateModelMixin):

    model = Appointments
    serializer_class = AppointmentNestedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id__id', 'escort_required', 'uuid',
                     'label_code', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'visitor_id__uuid',
                     'entrance_id')

    def get_queryset(self):

        queryset = Appointments.objects.all()

        uuid = self.request.QUERY_PARAMS.get('uuid', None)
        visitor_id__uuid = self.request.QUERY_PARAMS.get('visitor_id__uuid', None)
        host_id__id = self.request.QUERY_PARAMS.get('host_id__id', None)
        is_approved = self.request.QUERY_PARAMS.get('is_approved', None)
        is_expired = self.request.QUERY_PARAMS.get('is_expired', None)
        label_code = self.request.QUERY_PARAMS.get('label_code', None)

        if uuid is not None:
            queryset = queryset.filter(uuid=uuid)
        if visitor_id__uuid is not None:
            queryset = queryset.filter(visitor_id__uuid=visitor_id__uuid)
        if host_id__id is not None:
            queryset = queryset.filter(host_id__id=host_id__id)
        if is_approved is not None:
            queryset = queryset.filter(is_approved=is_approved)
        if is_expired is not None:
            queryset = queryset.filter(is_expired=is_expired)
        if label_code is not None:
            queryset = queryset.filter(label_code=label_code)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView, mixins.CreateModelMixin):
    model = Appointments
    serializer_class = AppointmentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id', 'escort_required', 'label_code'
                     'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid', 'visitor_id')

    def get_queryset(self):

        queryset = Appointments.objects.all()

        uuid = self.request.QUERY_PARAMS.get('uuid', None)
        visitor_id__uuid = self.request.QUERY_PARAMS.get('visitor_id__uuid', None)
        host_id__id = self.request.QUERY_PARAMS.get('host_id__id', None)
        is_approved = self.request.QUERY_PARAMS.get('is_approved', None)
        is_expired = self.request.QUERY_PARAMS.get('is_expired', None)
        label_code = self.request.QUERY_PARAMS.get('label_code', None)

        if uuid is not None:
            queryset = queryset.filter(uuid=uuid)
        if visitor_id__uuid is not None:
            queryset = queryset.filter(visitor_id__uuid=visitor_id__uuid)
        if host_id__id is not None:
            queryset = queryset.filter(host_id__id=host_id__id)
        if is_approved is not None:
            queryset = queryset.filter(is_approved=is_approved)
        if is_expired is not None:
            queryset = queryset.filter(is_expired=is_expired)
        if label_code is not None:
            queryset = queryset.filter(label_code=label_code)
        return queryset

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
                     'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid', 'visitor_id__uuid',
                     'label_code')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)