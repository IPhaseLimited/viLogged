from django.contrib.auth.views import login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, FormView
from braces.views import LoginRequiredMixin
from core.models import Appointments, UserProfile, Visitors
from core.forms.core_forms import AppointmentsForm, VisitorsForm
from django.http import HttpResponseRedirect, HttpResponse


class AppointmentsListView(LoginRequiredMixin, ListView):
    template_name = 'appointments/index.html'
    model = Appointments


class AppointmentsFormView(LoginRequiredMixin, FormView):
    template_name = 'appointments/form.html'

    def get(self, request, *args, **kwargs):

        context = super(AppointmentsFormView, self).get_context_data(**kwargs)
        context['form'] = AppointmentsForm()
        context['users_profile'] = UserProfile.objects.all()
        context['visitors'] = Visitors.objects.all()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = super(AppointmentsFormView, self).get_context_data(**kwargs)
        context['users_profile'] = UserProfile.objects.all()
        context['visitors'] = Visitors.objects.all()
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            new_appointment = form.save()

            return HttpResponseRedirect("/appointments/")
        else:
            context['form'] = form
            return render(request, self.template_name, context)