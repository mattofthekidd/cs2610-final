from __future__ import unicode_literals

import datetime

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Item(models.Model):
    command_name = models.CharField(max_length=200)
    command_opt = models.CharField(max_length=300)
    link_ref = models.URLField(max_length=10000)
    description = models.TextField(max_length=200)
    example = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __hash__(self):
        return self