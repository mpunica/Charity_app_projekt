"""
Django views for charity_app.
"""

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from .models import Donation, Institution

class LandingPage(View):
    """
    Main view
    """
    def get(self, request):
        donations = Donation.objects.all()
        institutions = Institution.objects.all()
        return render(request, "index.html", context= {'donations_amount': donations.count(), 'institutions_amount': institutions.count(), 'institutions_1': institutions[0]})


class AddDonation(View):
    """
    Add new Donation
    """
    def get(self, request):
        return render(request, "form.html")

class Login(View):
    """
    Login view
    """
    def get(self, request):
        return render(request, "login.html")

class Register(View):
    """
    Register view
    """
    def get(self, request):
        return render(request, "register.html")

