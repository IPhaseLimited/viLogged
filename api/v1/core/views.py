from rest_framework import serializers, generics, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from staff.views import UserProfile
from api.permissions import *