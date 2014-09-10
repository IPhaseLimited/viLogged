from django.contrib.auth.views import login_required, login as django_login, logout as django_logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from braces.views import LoginRequiredMixin
from core.models import Visitors, VisitStatus, VisitorsLocation, VisitorGroup, Vehicle


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class VisitorsListView(LoginRequiredMixin, ListView):
    template_name = 'visitors/index.html'
    model = Visitors

    def get_queryset(self):
        query = self.model.objects.all().select_related()
        return query

class Reports(LoginRequiredMixin, ListView):
    template_name = 'documents/index.html'
    model = Visitors

    def get_queryset(self):
        query = self.model.objects.all().select_related()
        return query

@login_required
def visitors_list_page(request):
    return render(request, 'visitors/index.html', {})


@login_required
def add_visitor(request):
    return render(request, 'visitors/form.html', {})


def login(req, template_name=''):
    return django_login(req, **{"template_name": 'login.html'})


def logout(req, template_name=''):
    django_logout(req, **{"template_name": 'login.html'})
    return redirect('/')
