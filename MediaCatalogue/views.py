from django.views.generic.base import TemplateView
from django_propeller.views import NavBarMixin

from .navbars import MainNavBar


class MainNavView(TemplateView, NavBarMixin):
    navbar_class = MainNavBar


class IndexPage(MainNavView):
    template_name = 'index.html'
