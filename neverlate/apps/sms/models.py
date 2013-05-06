from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.models import modelform_factory
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _



class Reminder_Options(models.Model):

    options = (("24hours", "24hours"), ("15minutes", "15minutes"))

class Recurring_Options(models.Model):

    options = (("24hours", "24hours"), ("15minutes", "15minutes"))



class Event(models.Model):

    name = models.CharField(_("Name"), max_length=40)
    phone = models.CharField(_("Phone"), max_length=10)
    event_datetime = models.DateTimeField(_("Date/Time"))
    reminder_datetime = models.DateTimeField(_("Date/Time"))
    reminder_options = models.ManyToManyField(Reminder_Options)
    message = models.CharField(_("Message"), max_length=160)
    recurring_options = models.ManyToManyField(Recurring_Options)
    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return u'/create-event/'


class EventForm(ModelForm):
    class Meta:
        model = Event   
