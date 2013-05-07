from django.contrib import admin
from django.contrib.admin import site
from apps.sms import models

site.register(models.Calendar)
site.register(models.Contact)
site.register(models.Event)
site.register(models.Message)