from django.db import models
from django.contrib.auth.models import User
from mixin_tools.history import HistoryFieldsMixin


# Create your models here.
class CompanyDepartments(HistoryFieldsMixin):
    department_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{}'.format(self.department_name)


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, default=1)
    phone = models.IntegerField(max_length=50)
    department = models.ForeignKey(CompanyDepartments, to_field='uuid', blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{}'.format(self.user_id.username)


class CompanyEntranceNames(HistoryFieldsMixin):
    entrance_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{}'.format(self.entrance_name)


class VisitorGroup(HistoryFieldsMixin):
    group_name = models.CharField(max_length=50)
    black_listed = models.BooleanField(default=False)

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{0}'.format(self.group_name)


class Visitors(HistoryFieldsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    visitors_email = models.EmailField(max_length=50, unique=True)
    visitors_phone = models.IntegerField(max_length=20)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    state_of_origin = models.CharField(max_length=50, blank=True, null=True)
    lga = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.ImageField(upload_to='images', blank=True, null=True)
    fingerprint = models.ImageField(upload_to='finger_prints', max_length=100, blank=True, null=True)
    scanned_signature = models.ImageField(upload_to='signature', max_length=100, blank=True, null=True)
    visitors_pass_code = models.CharField(max_length=50, blank=True, null=True)
    group_id = models.ForeignKey(VisitorGroup, to_field='uuid')

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class VisitorsLocation(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, to_field="uuid", blank=True, null=True)
    state = models.IntegerField(max_length=5)
    lga = models.IntegerField(max_length=5)
    contact_address = models.CharField(max_length=100)


class VisitStatus(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, blank=True, null=True, to_field="uuid")
    checked_in = models.DateTimeField(default="0000-00-00 00:00:00", blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    entrance_id = models.ForeignKey(CompanyEntranceNames, blank=True, null=True, to_field="uuid")


class Appointments(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, to_field="uuid")
    representing = models.CharField(max_length=100)
    purpose = models.CharField(max_length=50)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    visit_start_time = models.TimeField()
    visit_end_time = models.TimeField()
    host_id = models.ForeignKey(UserProfile, blank=True, null=True)
    escort_required = models.BooleanField(default=False)


class AppointmentsStatus(HistoryFieldsMixin):
    appointment_id = models.ForeignKey(Appointments, blank=True, null=True, to_field="uuid")
    approved = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)


class Vehicle(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, blank=True, null=True, to_field="uuid")
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
    linked_user = models.ForeignKey(Visitors, to_field='uuid', blank=True, null=True)
    checked_in = models.DateTimeField(blank=True, null=True, default="0000-00-00 00:00:00")
    checked_out = models.DateTimeField(blank=True, null=True, default="0000-00-00 00:00:00")