from rest_framework import serializers, generics
from api.serializer import UUIDRelatedField
from core.models import RestrictedItems, Vehicle, CompanyDepartments, CompanyEntranceNames


class RestrictedItemsSerializer(serializers.ModelSerializer):
    appointment_id = UUIDRelatedField(many=False)

    class Meta:
        model = RestrictedItems
        fields = ('item_type', 'item_name', 'item_code', 'appointment_id', 'uuid', 'created', 'modified_by',
                  'created_by', 'modified')
        lookup_field = 'uuid'


class VehicleSerializer(serializers.ModelSerializer):
    appointment_id = UUIDRelatedField(many=False)

    class Meta:
        model = Vehicle
        fields = ('appointments_id', 'license', 'model', 'vehicle_type', 'color', 'uuid', 'created', 'modified_by',
                  'created_by', 'modified')
        lookup_field = 'uuid'


class CompanyDepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyDepartments
        fields = ('department_name', 'description', 'uuid', 'created', 'modified_by', 'created_by', 'modified')
        lookup_field = 'uuid'


class CompanyEntranceNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyEntranceNames
        fields = ('entrance_name', 'uuid', 'created', 'modified_by', 'created_by', 'modified')
        lookup_field = 'uuid'