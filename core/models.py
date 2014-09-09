from django.db import models
from django.contrib.auth.models import User
from mixin_tools.history import HistoryFieldsMixin


# Create your models here.
class UserProfile(models.Model):
    user_id = models.ForeignKey(User, default=1)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100)


class CompanyEntranceNames(HistoryFieldsMixin):
    entrance_name = models.CharField(max_length=50)


class CompanyDepartments(HistoryFieldsMixin):
    department_name = models.CharField(max_length=100)
    department_head = models.ForeignKey(UserProfile, blank=True, null=True)


class Visitors(HistoryFieldsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    visitors_email = models.CharField(max_length=50, unique=True)
    visitors_phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    state_of_origin = models.IntegerField(max_length=5, blank=True, null=True)
    lga = models.IntegerField(max_length=5, blank=True, null=True)
    image_url = models.CharField(max_length=100, blank=True, null=True)
    fingerprint = models.CharField(max_length=100, blank=True, null=True)
    visitors_pass_code = models.CharField(max_length=50, blank=True, null=True)


class VisitorGroup(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, blank=True, null=True)
    GROUP_TYPES = (
        ('VIP',) * 2,
        ('Black Listed',) * 2,
        ('Normal',) * 2, )
    group_type = models.CharField(max_length=50, choices=GROUP_TYPES)


class VisitorsLocation(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, blank=True, null=True)
    state = models.IntegerField(max_length=5)
    lga = models.IntegerField(max_length=5)
    contact_address = models.CharField(max_length=100)


class VisitStatus(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, blank=True, null=True)
    Checked_in = models.DateTimeField()
    checked_out = models.DateTimeField()
    entrance_id = models.ForeignKey(CompanyEntranceNames, blank=True, null=True)


class Appointments(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors)
    representing = models.CharField(max_length=100)
    purpose = models.CharField(max_length=50)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    visit_start_time = models.TimeField()
    visit_end_time = models.TimeField()
    host_id = models.ForeignKey(UserProfile, blank=True, null=True)
    escort_required = models.BooleanField(default=True)


class AppointmentsStatus(HistoryFieldsMixin):
    appointment_id = models.ForeignKey(Appointments, blank=True, null=True)
    approved = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)


class Vehicle(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, blank=True, null=True)
    license = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    tank_size = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=20, blank=True, null=True)


class MessageQueue(HistoryFieldsMixin):
    message_body = models.TextField()
    destination = models.CharField(max_length=50)
    source = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)


class AppLicenseDuration(models.Model):
    licenseKey = models.TextField()
    app_start_date = models.DateField()
    app_duration_days = models.IntegerField()


class DocumentManagement(HistoryFieldsMixin):
    document_type = models.CharField(max_length=100)
    document_name = models.CharField(max_length=50)
    document_code = models.CharField(max_length=50)
    linked_user = models.IntegerField(max_length=5)