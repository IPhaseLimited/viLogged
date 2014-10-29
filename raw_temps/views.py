import json
import datetime
from django.contrib import messages
from django.contrib.auth.views import login_required, login as django_login, logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, FormView
from braces.views import LoginRequiredMixin
from core.models import Visitors, VisitorsLocation, Vehicle, Appointments
from core.forms.core_forms import *
from core.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from lib.utility import Utility
from viLogged.settings import MEDIA_ROOT


class JSONResponseMixin(object):
    def render_json(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

@login_required
def staff_form(request, *args, **kwargs):

    return render(request, 'staff/raw-from.html', {})
