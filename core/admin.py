from django.contrib import admin
from django.contrib.auth.models import User
import uuid
from core.models import *


class UserProfileAdmin(admin.StackedInline):
    list_display = ('user_id', 'phone', 'image', 'department', 'designation')
    model = UserProfile


class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileAdmin]


class VisitorsAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'created_by')
    list_display = ('first_name', 'last_name', 'visitors_email', 'visitors_phone', 'date_of_birth', 'created',
                    'state_of_origin', 'lga_of_origin', 'image', 'occupation', 'company_name', 'company_address',
                    'fingerprint', 'scanned_signature', 'visitors_pass_code',)

    #prepopulated_fields = {'uuid': (uuid.uuid4(),)}
    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()


class VisitorGroupAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'created_by')
    list_display = ('group_name', 'black_listed')

    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()


class VisitorsLocationAdmin(admin.ModelAdmin):
    list_display = ('visitor_id', 'residential_state', 'residential_lga', 'contact_address')
    readonly_fields = ('uuid', 'created_by')

    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('visitor_id', 'representing', 'purpose', 'appointment_date', 'visit_start_time',
                    'visit_end_time', 'host_id', 'escort_required', 'is_approved', 'is_expired', 'checked_in', 'checked_out',
                    'entrance_id')
    readonly_fields = ('uuid', 'created_by')

    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('appointments_id', 'license', 'model', 'vehicle_type', 'color',)
    readonly_fields = ('uuid', 'created_by')

    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()


class RestrictedItemsManagementAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'item_name', 'item_code', 'appointment_id',)
    readonly_fields = ('uuid', 'created_by')

    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()


class CompanyEntranceNamesAdmin(admin.ModelAdmin):
    list_display = ('entrance_name',)
    readonly_fields = ('uuid', 'created_by')

    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()


class CompanyDepartmentsAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'description')
    readonly_fields = ('uuid', 'created_by')

    def save_model(self, request, obj, form, change):
        if obj.uuid is None:
            obj.uuid = uuid.uuid4()
            obj.created_by = request.user
        obj.save()

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Visitors, VisitorsAdmin)
admin.site.register(VisitorGroup, VisitorGroupAdmin)
admin.site.register(VisitorsLocation, VisitorsLocationAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Appointments, AppointmentsAdmin)
admin.site.register(RestrictedItems, RestrictedItemsManagementAdmin)
admin.site.register(CompanyEntranceNames, CompanyEntranceNamesAdmin)
admin.site.register(CompanyDepartments, CompanyDepartmentsAdmin)