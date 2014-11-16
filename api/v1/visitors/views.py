from rest_framework import serializers, generics, mixins, views
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.models import Visitors, VisitorGroup, VisitorsLocation
from api.permissions import *
from api.serializer import *


class VisitorsLocationSerializer(serializers.ModelSerializer):
    visitor_id = UUIDRelatedField(many=False)

    class Meta:
        model = VisitorsLocation
        fields = ('visitor_id', 'residential_country', 'residential_state', 'residential_state', 'residential_lga', 'contact_address', 'uuid')
        lookup_field = 'uuid'
        filter_fields = ('visitor_id',)


class VisitorSerializer(serializers.ModelSerializer):
    group_id = UUIDRelatedField()

    class Meta:
        model = Visitors
        fields = ('first_name', 'last_name', 'visitors_email', 'visitors_phone', 'date_of_birth',
                  'state_of_origin', 'lga_of_origin', 'image_url', 'occupation', 'company_name', 'company_address',
                  'fingerprint', 'scanned_signature', 'visitors_pass_code', 'nationality', 'uuid',)
        lookup_field = 'uuid',
        filter_fields = ('first_name', 'last_name', 'visitors_email', 'visitors_phone', 'visitors_pass_code',
                         'fingerprint', 'scanned_signature', 'date_of_birth',)


class VisitorNestedSerializer(serializers.ModelSerializer):
    current_location = VisitorsLocationSerializer(many=True)

    class Meta:
        model = Visitors
        fields = ('first_name', 'last_name', 'visitors_email', 'visitors_phone', 'date_of_birth',
                  'state_of_origin', 'lga_of_origin', 'image_url', 'occupation', 'company_name', 'company_address',
                  'fingerprint', 'scanned_signature', 'visitors_pass_code', 'nationality', 'uuid', 'current_location')
        lookup_field = 'uuid'


class VisitorsLocationList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,):
    queryset = VisitorsLocation.objects.all()
    serializer_class = VisitorsLocationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VisitorsLocationDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                             generics.GenericAPIView, mixins.CreateModelMixin):

    queryset = VisitorsLocation.objects.all()
    serializer_class = VisitorsLocationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorsList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,):

    queryset = Visitors.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VisitorsNestedList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,):

    queryset = Visitors.objects.all()
    serializer_class = VisitorNestedSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VisitorNestedDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Visitors.objects.all()
    serializer_class = VisitorNestedSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Visitors.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorOwnDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Visitors.objects.all()
    serializer_class = VisitorSerializer
    lookup_field = 'visitor_pass_code'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthenticateVisitor(views.APIView):

    def post(self, request):
        return Response({'error_message': '', 'message': 'message was queued to be sent'})