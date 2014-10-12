from django import forms
from core.models import *
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
import uuid
User = get_user_model()

class UserProfileFrom(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_id', 'phone', 'image_url', 'department', 'designation', 'home_phone', 'work_phone')

        widgets = {
            'user_id': forms.Select(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'work_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'home_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", 'last_name', 'first_name')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = ['first_name', 'last_name', 'visitors_email', 'visitors_phone', 'date_of_birth', 'group_id',
                  'state_of_origin', 'lga', 'image_url', 'occupation', 'company_name', 'company_address',
                  'fingerprint', 'scanned_signature', 'visitors_pass_code', 'nationality']

    def save(self, commit=True):
        visitor = super(VisitorsForm, self).save(commit=False)
        if visitor.uuid is None:
            visitor.uuid = uuid.uuid4()
        if commit:
            visitor.save()
        return visitor

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['visitor_id', 'representing', 'purpose', 'arrival_date', 'departure_date', 'visit_start_time',
                  'visit_end_time', 'host_id', 'escort_required', 'approved', 'expired', 'checked_in', 'checked_out',
                  'entrance_id']

    def save(self, commit=True):
        appointment = super(AppointmentsForm, self).save(commit=False)
        if appointment.uuid is None:
            appointment.uuid = uuid.uuid4()
        if commit:
            appointment.save()
        return appointment

    def clean(self):
        cleaned_data = super(AppointmentsForm, self).clean()
        visit_start_time = cleaned_data.get("visit_start_time")
        visit_end_time = cleaned_data.get("visit_end_time")
        arrival_date = cleaned_data.get("arrival_date")
        departure_date = cleaned_data.get("departure_date")

        if departure_date < arrival_date:
            self._errors['departure_date'] = u"Departure date must not be less than Arrival date"
            self._errors['arrival_date'] = u"Arrival date must not be greater than Departure date"
            del cleaned_data["departure_date"]
            del cleaned_data["arrival_date"]

        if visit_end_time < visit_start_time:
            self._errors['visit_end_time'] = u"Appointment end time date must not be less than Appointment start time"
            self._errors['visit_start_time'] = u"Appointment start time date must not be greater than Appointment end" \
                                               u" time"
            del cleaned_data["visit_end_time"]
            del cleaned_data["visit_start_time"]

        # Always return the full collection of cleaned data.
        return cleaned_data