from django import forms
from core.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import uuid


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
        fields = ("username", "email", "password1", "password2", 'last_name', 'first_name', 'is_superuser')

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
