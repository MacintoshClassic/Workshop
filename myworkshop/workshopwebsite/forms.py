from unittest.util import _MAX_LENGTH
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


class Addclient(forms.Form):
    name = forms.CharField(label="Your name")
    phone = forms.CharField(label="Your telephone number")


class Addcar(forms.Form):
    number = forms.CharField(label="Car registration number")
    model = forms.CharField(label="Car model")
    year = forms.CharField(label="Car year")


class Addorder(forms.Form):
    name = forms.CharField(label="Your name")
    phone = forms.CharField(label="Your telephone number")
    number = forms.CharField(label="Car registration number")
    model = forms.CharField(label="Car model")
    year = forms.CharField(label="Car year")
    issue_description = forms.CharField(label="Issue description")


class Checkyourorder(forms.Form):
    client = forms.CharField(label="Your id")


class Choosemechanic(forms.Form):
    id = forms.CharField(label="Input your order id")
    mechanic = forms.CharField(label="Pick the mechanic")


class ChooseFinishingDate(forms.Form):
    id = forms.CharField(label="Input your order id")
    price = forms.CharField(label="Input price")
    finishing_date = forms.CharField(label="Input finishing date")
