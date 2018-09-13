# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def create_user(self, name, email, password, confirm_password):
        user = self.create(name=name, email=email, password=password, confirm_password=confirm_password)
        return user

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    objects = UserManager()
    def __str__(self):
        return self.name
