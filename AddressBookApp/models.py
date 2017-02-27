from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Information(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=100)
    qq = models.CharField(max_length=20)