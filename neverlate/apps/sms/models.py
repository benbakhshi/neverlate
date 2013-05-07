from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.models import modelform_factory
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class ReminderOptions(object):
    day         = 1440
    two_hours   = 120
    one_hour    = 60
    half_hour   = 30

    CHOICES = (
                (day, "One Day Before"),
                (two_hours, "Two Hours Before"),
                (one_hour, "One Hour Before"),
                (half_hour, "Half Hour Before"),
            )

# class RecurringOptions(object):
#
#     daily = 1440
#     b = 10080
#
#     CHOICES = ((a, "24hours"),
#                (b, "1week")
#                 )


class Message(models.Model):
    title = models.CharField(max_length=160)

    def __unicode__(self):
        return self.title

class Calendar(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="calendar")
    title = models.CharField(default="My Calendar", max_length=100)
    messages = models.ForeignKey(Message, default=1)
    timezone = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.title

class Contact(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="contact")
    name = models.CharField(_("Recipient"), max_length=40)
    phone = models.IntegerField(_("Phone"), max_length=10)

    def __unicode__(self):
        return "%s: %d" % (self.name, self.phone)

class Event(models.Model):
    calendar = models.ForeignKey(Calendar, verbose_name=_("Calendar"), related_name="event_calendar")
    message = models.ForeignKey(Message, verbose_name=_("Message"), related_name="event_message")
    recipient = models.ForeignKey(Contact, verbose_name=_("Recipient"), related_name="event1")
    event_date = models.DateField(_("Date"))
    start_time = models.TimeField(_("Start time"))
    end_time = models.TimeField(_("End time"), blank=True, null=True)
    location = models.CharField(_("Location of meeting"), blank=True, null=True, max_length=100)
    reminder_options = models.IntegerField(choices=ReminderOptions.CHOICES, verbose_name=_("Reminder time"))
    content = models.CharField(_("Event Notes"), max_length=160)
    # recurring_options = models.IntegerField(choices=RecurringOptions.CHOICES, verbose_name=_("Recurring time"))

    def __unicode__(self):
        return self.recipient

    def get_absolute_url(self):
        return u'/create-event/'


# class EventForm(ModelForm):
#     class Meta:
#         model = Event

