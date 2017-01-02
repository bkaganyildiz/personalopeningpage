from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from .choices import *

class Component(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Background(Component) :
    image = models.ImageField(upload_to = '', default = 'no-image.png')

    def __str__(self):
        return self.name

class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(choices=CONNECTION_CHOICES, max_length=25, default="")

    def __str__(self):
        return self.url

class PersonalInfo(Component):
    image = models.ImageField()
    info = models.CharField(max_length=500)


    def __str__(self):
        return self.name