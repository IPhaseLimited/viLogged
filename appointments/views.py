from django.contrib.auth.views import login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from braces.views import LoginRequiredMixin
from core.models import Appointments

@login_required
def get_all_appointments(request):
    return render(request, 'appointments/index.html', {})


class AppointmentsListView(LoginRequiredMixin, ListView):
    template_name = 'appointments/index.html'
    model = Appointments

