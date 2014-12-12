from django.db import models
from django.contrib.auth.models import User
from mixin_tools.history import HistoryFieldsMixin
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


# Create your models here.
class CompanyDepartments(HistoryFieldsMixin):
    department_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='department_modified_by')

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{}'.format(self.department_name)


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, unique=True, blank=True, null=True, related_name='user_profile')
    gender = models.CharField(max_length=10, default='Male')
    phone = models.CharField(max_length=20, unique=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{}'.format(self.user_id.username)


class CompanyEntranceNames(HistoryFieldsMixin):
    entrance_name = models.CharField(max_length=50, unique=True)
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='entrance_modified_by')

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{}'.format(self.entrance_name)


class VisitorGroup(HistoryFieldsMixin):
    group_name = models.CharField(max_length=50, unique=True)
    black_listed = models.BooleanField(default=False)
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='group_modified_by')

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{0}'.format(self.group_name)


class Visitors(HistoryFieldsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    visitors_email = models.EmailField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, default='Male')
    visitors_phone = models.CharField(max_length=20, unique=True, verbose_name='visitors phone number')
    occupation = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    state_of_origin = models.CharField(max_length=50, blank=True, null=True)
    lga_of_origin = models.CharField(max_length=50, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    fingerprint = models.TextField(blank=True, null=True)
    scanned_signature = models.TextField(blank=True, null=True)
    visitors_pass_code = models.CharField(max_length=50, blank=True, null=True)
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='visitor_modified_by')
    group_type = models.ForeignKey(VisitorGroup, to_field='uuid', related_name='group', null=True, blank=True)

    class Meta:
        app_label = 'core'

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class VisitorsLocation(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, to_field="uuid", blank=True, null=True, related_name='current_location')
    residential_country = models.CharField(max_length=20)
    residential_state = models.CharField(max_length=50)
    residential_lga = models.CharField(max_length=50)
    contact_address = models.CharField(max_length=100)
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='location_modified_by')


class Appointments(HistoryFieldsMixin):
    visitor_id = models.ForeignKey(Visitors, to_field="uuid", related_name="visitor")
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='appointment_modified_by')
    representing = models.CharField(max_length=100, blank=True, null=True)
    purpose = models.CharField(max_length=50, blank=True, null=True)
    appointment_date = models.DateField()
    visit_start_time = models.TimeField()
    visit_end_time = models.TimeField()
    host_id = models.ForeignKey(User, blank=True, null=True, related_name="host")
    escort_required = models.BooleanField(default=False)
    is_approved = models.IntegerField(default=None, null=True, blank=True)
    is_expired = models.BooleanField(default=False)
    checked_in = models.DateTimeField(default=None, blank=True, null=True)
    checked_out = models.DateTimeField(blank=True, null=True)
    label_code = models.CharField(max_length=50, null=True, blank=True)
    entrance_id = models.ForeignKey(CompanyEntranceNames, blank=True, null=True, to_field="uuid",
                                    related_name="entrance")


class Vehicle(HistoryFieldsMixin):
    appointments_id = models.ForeignKey(Appointments, blank=True, null=True, to_field="uuid", related_name='vehicle')
    license = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(blank=True, null=True, max_length=20)
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='vehicle_modified_by')


class MessageQueue(HistoryFieldsMixin):
    message_body = models.TextField()
    destination = models.CharField(max_length=50)
    subject = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(default=0)
    type = models.IntegerField(max_length=2, default=0)
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='message_modified_by')


class AppLicenseDuration(models.Model):
    licenseKey = models.TextField()
    app_start_date = models.DateField()
    app_duration_days = models.IntegerField()


class RestrictedItems(HistoryFieldsMixin):
    item_type = models.CharField(max_length=100)
    item_name = models.CharField(max_length=50)
    item_code = models.CharField(max_length=50)
    appointment_id = models.ForeignKey(Appointments, blank=True, null=True, related_name="restricted_items")
    modified_by = models.ForeignKey('auth.User', null=True, blank=True, related_name='items_modified_by')