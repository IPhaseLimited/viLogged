import json
import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, FormView
from braces.views import LoginRequiredMixin
from core.forms.core_forms import *
from core.models import UserProfile
from django.contrib.auth.models import User


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


class StaffsListView(LoginRequiredMixin, ListView):
    template_name = 'staff/index.html'
    model = UserProfile

    def get_queryset(self):
        query = self.model.objects.all().select_related()
        return query


class StaffFormView(LoginRequiredMixin, FormView):
    template_name = 'staff/form.html'

    def get(self, request, *args, **kwargs):
        url_name = self.request.resolver_match.url_name
        if url_name is 'staff_edit_pk':

            user_data = User.objects.get(id=self.kwargs['pk'])
            try:
                user_profile = UserProfile.objects.get(user_id__id=user_data.id)
            except UserProfile.DoesNotExist:
                user_profile = {}

        elif url_name is 'staff_edit':
            user_data = User.objects.get(id=request.user.id)
            try:
                user_profile = UserProfile.objects.get(user_id__id=request.user.id)
            except UserProfile.DoesNotExist:
                user_profile = {}

        else:
            user_data = {}
            user_profile = {}

        context = super(StaffFormView, self).get_context_data(**kwargs)
        context['form'] = UserCreateForm(instance=user_data)
        context['profile_form'] = UserProfileFrom(instance=user_profile)
        context['departments'] = CompanyDepartments.objects.all()
        context['user_id'] = request.user.id
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        url_name = self.request.resolver_match.url_name
        if url_name is 'staff_edit_pk':

            user_data = User.objects.get(id=self.kwargs['pk'])
            try:
                user_profile = UserProfile.objects.get(user_id__id=user_data.id)
            except UserProfile.DoesNotExist:
                user_profile = {}

        elif url_name is 'staff_edit':
            user_data = User.objects.get(id=request.user.id)
            try:
                user_profile = UserProfile.objects.get(user_id__id=request.user.id)
            except UserProfile.DoesNotExist:
                user_profile = {}

        else:
            user_data = {}
            user_profile = {}

        context = super(StaffFormView, self).get_context_data(**kwargs)
        context['departments'] = CompanyDepartments.objects.all()
        context['post_data'] = request.POST
        profile_form = UserProfileFrom(request.POST, instance=user_profile)
        form = UserCreateForm(request.POST, instance=user_data)
        if form.is_valid() and profile_form.is_valid():
            new_user = form.save()
            new_user.email = request.POST.get('username')
            new_user.save()
            try:
                department_id = CompanyDepartments.objects.get(uuid=request.POST.get('department'))
            except CompanyDepartments.DoesNotExist:
                department_id = None

            user_profile = UserProfile(
                user_id=new_user,
                phone=request.POST.get('phone'),
                home_phone=request.POST.get('home_phone'),
                work_phone=request.POST.get('office_phone'),
                department=department_id,
                designation=request.POST.get('designation')
            )
            user_profile.save()

            return HttpResponseRedirect("/staff-list/")
        else:
            context['form'] = form
            context['profile_form'] = profile_form
            return render(request, self.template_name, context)


def user_profile_view(request, *args, **kwargs):
    template_name = 'staff/profile.html'
    context = {}
    if request.is_ajax():
        appointment = Appointments.objects.get(uuid=kwargs['uuid'])
        appointment.approved = True
        appointment.save()
        approved_list = Appointments.objects.all().filter(approved=True, host_id=kwargs['pk'])
        html = ""
        for approved in approved_list:
            html += '<tr id="approve-{}">'.format(approved.uuid)
            html += '  <td><a id="view-visitor-detail" class="pointer">{0} {1}</a></td>'.format(approved.visitor_id.first_name, approved.visitor_id.last_name)
            html += '  <td>{}</td>'.format(approved.visitor_id.visitors_phone)
            html += '  <td>{0} {1}</td>'.format(approved.arrival_date, approved.visit_start_time)
            html += '  <td>{0} {1}</td>'.format(approved.departure_date, approved.visit_end_time)
            html += '</tr>'
        data = json.dumps({"html": html})

        return HttpResponse(data, content_type='application/json')

    else:
        try:
            user_profile = UserProfile.objects.get(id=kwargs['pk'])
        except KeyError:
            user_profile = User.objects.filter(userprofile__user_id=request.user.id).get(id=request.user.id)

        context['awaiting_approval'] = Appointments.objects.all().filter(approved=False, host_id=user_profile.id)
        context['approved'] = Appointments.objects.all().filter(approved=True, host_id=user_profile.id)
        context['profile'] = user_profile
        context['context'] = context
        return render(request, template_name, context)