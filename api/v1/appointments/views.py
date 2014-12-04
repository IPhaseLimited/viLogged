from rest_framework import serializers, generics, mixins
from core.models import Appointments, RestrictedItems, Vehicle, CompanyEntranceNames
from api.v1.core.serializers import CompanyEntranceNamesSerializer, VehicleSerializer, RestrictedItemsSerializer
from api.permissions import *
from api.serializer import *
from api.v1.visitors.views import VisitorSerializer
from api.v1.user.views import UserNestedSerializer, UserProfileNestedSerializer


def filter_from_url(query_params):
    queryset = Appointments.objects.all()

    uuid = query_params.get('uuid', None)
    visitor_id__uuid = query_params.get('visitor_id__uuid', None)
    host_id__id = query_params.get('host_id__id', None)
    is_approved = query_params.get('is_approved', None)
    is_expired = query_params.get('is_expired', None)
    label_code = query_params.get('label_code', None)
    host_id = query_params.get('host_id', None)
    visitor_id = query_params.get('visitor_id', None)

    def str_to_bool(s):
        if s == 'True' or s == 'true':
            return True
        elif s == 'False' or s == 'false':
            return False


    def str_to_bool2(s):

        if s == 'True' or s == 'true' or s == '1':
            return 1
        elif s == 'False' or s == 'false' or s == '0':
            return 0
        else:
            raise ValueError

    if uuid is not None:
        queryset = queryset.filter(uuid=uuid)
    if visitor_id__uuid is not None:
        queryset = queryset.filter(visitor_id__uuid=visitor_id__uuid)
    if host_id__id is not None:
        queryset = queryset.filter(host_id__id=host_id__id)
    if is_approved is not None:
        queryset = queryset.filter(is_approved=str_to_bool2(is_approved))
    if is_expired is not None:
        queryset = queryset.filter(is_expired=str_to_bool(is_expired))
    if label_code is not None:
        queryset = queryset.filter(label_code=label_code)
    if host_id is not None:
        queryset = queryset.filter(host_id=host_id)
    if visitor_id is not None:
        queryset = queryset.filter(visitor_id=visitor_id)

    return queryset


class AppointmentSerializer(serializers.ModelSerializer):
    visitor_id = UUIDRelatedField(many=False)
    entrance_id = UUIDRelatedField(many=False)
    class Meta:
        model = Appointments
        fields = ('visitor_id', 'representing', 'purpose', 'appointment_date', 'visit_start_time', 'visit_end_time',
                  'host_id', 'escort_required', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id',
                  'uuid', 'label_code', 'created', 'modified_by', 'created_by', 'modified')


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
                  'visitor_id', 'vehicle', 'restricted_items', 'label_code', 'created', 'modified_by', 'created_by',
                  'modified')


class AppointmentList(generics.ListAPIView, mixins.CreateModelMixin):

    model = Appointments
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #lookup_field = 'uuid'
    filter_fields = ('appointment_date', 'visit_start_time', 'visit_end_time', 'host_id', 'escort_required',
                     'label_code', 'is_approved', 'is_expired', 'checked_in', 'checked_out', 'entrance_id', 'uuid',
                     'visitor_id')

    def get_queryset(self):

        return filter_from_url(self.request.QUERY_PARAMS)

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

        return filter_from_url(self.request.QUERY_PARAMS)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AppointmentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView, mixins.CreateModelMixin):
    model = Appointments
    serializer_class = AppointmentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'

    def get_queryset(self):

        return filter_from_url(self.request.QUERY_PARAMS)

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

    def get_queryset(self):

        return filter_from_url(self.request.QUERY_PARAMS)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)