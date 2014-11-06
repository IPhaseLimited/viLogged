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


def home(request, *args, **kwargs):
    data = json.dumps({"message":"nothing to see here"})
    return HttpResponse(data, content_type='application/json')


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class VisitorsListView(LoginRequiredMixin, ListView):
    template_name = 'visitors/index.html'
    model = Visitors

    def get_queryset(self):
        query = self.model.objects.all().select_related()
        return query


class VisitorsFormView(LoginRequiredMixin, FormView):
    template_name = 'visitors/form.html'

    def get(self, request, *args, **kwargs):

        context = super(VisitorsFormView, self).get_context_data(**kwargs)
        context['form'] = VisitorsForm()
        context['users_profile'] = UserProfile.objects.all()
        context['groups'] = VisitorGroup.objects.all()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = super(VisitorsFormView, self).get_context_data(**kwargs)
        context['users_profile'] = UserProfile.objects.all()
        context['groups'] = VisitorGroup.objects.all()
        form = VisitorsForm(request.POST)
        if form.is_valid():
            new_visitor = form.save()

            return HttpResponseRedirect("/visitors/")
        else:
            context['form'] = form
            return render(request, self.template_name, context)


class Reports(LoginRequiredMixin, TemplateView):
    template_name = 'reports/index.html'
    model = Visitors

    def get_queryset(self):
        query = self.model.objects.all().select_related()
        return query


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'staff/profile.html'

    def get(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        try:
            user_profile = UserProfile.objects.get(id=self.kwargs['pk'])

        except KeyError:
            user_profile = UserProfile.objects.get(user_id=request.user.id)

        context['profile'] = user_profile
        return render(request, self.template_name, context)


@login_required
def add_visitor(request):
    return render(request, 'visitors/form.html', {})


def login(req, template_name=''):
    return django_login(req, **{"template_name": 'login.html'})


def logout(req, template_name=''):
    django_logout(req, **{"template_name": 'login.html'})
    return redirect('/')



@csrf_exempt
def send_email(request):
    sent = Utility.send_email('Test Mail', 'test is cool', ['musa@musamusa.com'])
    return HttpResponse('mail sent is {}'.format(sent))


def sms(request):
    sent = Utility.sms()
    return HttpResponse('sms sent is {}'.format(sent))


def load_bar_code(request):
    filename = MEDIA_ROOT+'/img/ean13.png'
    str_name = Utility.create_barcode('123344555')
    context = {}
    context['image_code'] = str_name
    return render(request, 'test_image.html', context)


def label(request):
    filename = MEDIA_ROOT+'/img/ean13.png'
    str_name = Utility.create_barcode('0000001')
    context = {'image_code': str_name}
    return render(request, 'lable.html', context)