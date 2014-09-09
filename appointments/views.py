from django.contrib.auth.views import login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin

@login_required
def get_all_appointments(request):
    return render(request, 'appointments/index.html', {})

