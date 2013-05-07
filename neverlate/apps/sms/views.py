from django import forms
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from pprint import pprint, pformat
from models import Event
from urllib import urlencode



class CreateEventView(CreateView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class EventListView(ListView):
    model = Event