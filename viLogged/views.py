from django.contrib.auth.views import login as django_login, logout as django_logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


def login(req, template_name=''):
    return django_login(req, **{"template_name": 'login.html'})


def logout(req, template_name=''):
    django_logout(req, **{"template_name": 'login.html'})
    return redirect('/')