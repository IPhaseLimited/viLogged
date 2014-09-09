from django.contrib.auth.views import login_required, login as django_login, logout as django_logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


@login_required
def visitors_list_page(request):
    return render(request, 'visitors/index.html', {})


@login_required
def add_visitor(request):
    return render(request, 'visitors/form.html', {})


@login_required
def login(req, template_name=''):
    return django_login(req, **{"template_name": 'login.html'})


@login_required
def logout(req, template_name=''):
    django_logout(req, **{"template_name": 'login.html'})
    return redirect('/')
