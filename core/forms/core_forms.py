from django import forms
from core.models import *
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
import uuid
import json
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
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", 'last_name', 'first_name', 'id')
        exclude = ('password1', 'password2', 'password')


    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.email
        except User.DoesNotExist:
            pass

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if self.instance.id is None:
            if password1 == '':
                self._errors['password1'] = u'This field is required.'
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if self.instance.id is None:
            if password2 == '':
                self._errors['password2'] = u'This field is required.'

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        password = self.instance.password
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        if self.cleaned_data["password1"] == '':
            user.password = password
            user.save()
        return user

    def clean(self):

        cleaned_data = super(UserCreateForm, self).clean()
        return self.cleaned_data


class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = ['first_name', 'last_name', 'visitors_email', 'visitors_phone', 'date_of_birth', 'group_id',
                  'state_of_origin', 'lga_of_origin', 'image_url', 'occupation', 'company_name', 'company_address',
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
        fields = ['visitor_id', 'representing', 'purpose', 'appointment_date', 'visit_start_time',
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

        if visit_end_time < visit_start_time:
            self._errors['visit_end_time'] = u"Appointment end time date must not be less than Appointment start time"
            self._errors['visit_start_time'] = u"Appointment start time date must not be greater than Appointment end" \
                                               u" time"
            del cleaned_data["visit_end_time"]
            del cleaned_data["visit_start_time"]

        # Always return the full collection of cleaned data.
        return cleaned_data