from rest_framework import generics, status, views, mixins
from rest_framework.response import Response
from lib.utility import Utility
from core.models import MessageQueue, RestrictedItems, Vehicle, CompanyDepartments, CompanyEntranceNames
from api.permissions import *
from api.v1.core.serializers import CompanyDepartmentsSerializer, VehicleSerializer, CompanyEntranceNamesSerializer,\
    RestrictedItemsSerializer


class SendEmail(views.APIView):

    def post(self, request):
        errors = []

        subject = request.DATA.get('subject')
        email = request.DATA.get('email')
        message = request.DATA.get('message')
        if subject is None:
            errors.append('please provide mail subject')

        if message is None:
            errors.append('please provide mail message')

        if email is None:
            errors.append('please provide mail address')

        if len(errors):
            return Response({'error_message': ', '.join(errors)}, status=status.HTTP_400_BAD_REQUEST)

        mail_response = Utility.send_email(subject, message, [email])
        if mail_response:
            return Response({'error_message': '', 'message': 'message sent successfully'})
        queue = MessageQueue(
            destination=email,
            message_body=message,
            subject=subject,
            type=0
        )
        queue.save()
        return Response({'error_message': '', 'message': 'message was queued to be sent'})


class VehicleList(generics.ListAPIView, mixins.CreateModelMixin):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VehicleDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RestrictedItemsList(generics.ListAPIView, mixins.CreateModelMixin):

    queryset = RestrictedItems.objects.all()
    serializer_class = RestrictedItemsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RestrictedItemsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                            generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = RestrictedItems.objects.all()
    serializer_class = RestrictedItemsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CompanyDepartmentsList(generics.ListAPIView, mixins.CreateModelMixin):

    queryset = CompanyDepartments.objects.all()
    serializer_class = CompanyDepartmentsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CompanyDepartmentsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                               generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = CompanyDepartments.objects.all()
    serializer_class = CompanyDepartmentsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CompanyEntranceNamesList(generics.ListAPIView, mixins.CreateModelMixin):

    queryset = CompanyEntranceNames.objects.all()
    serializer_class = CompanyEntranceNamesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CompanyEntranceNamesDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                 generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = CompanyEntranceNames.objects.all()
    serializer_class = CompanyEntranceNamesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)