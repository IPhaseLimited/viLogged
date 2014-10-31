from rest_framework import serializers, generics, mixins, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from staff.views import UserProfile
from django.contrib.auth.models import User