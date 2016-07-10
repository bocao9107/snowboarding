from __future__ import unicode_literals
from django import forms
from django.db import models
import datetime
from time import time
# Create your models here.



class video(models.Model):
    title= models.CharField(max_length=200, unique=True)
    image=models.FileField(null=True, blank=True)
    descripton= models.TextField(max_length=800, blank=True,null=True)
    date= models.DateTimeField(default=datetime.datetime.now())

class learningsking(models.Model):
    title= models.CharField(max_length=200, unique=True)
    videos= models.ForeignKey(video)
    similar= models.ForeignKey("self", null=True, blank=True)
    descripton= models.TextField(max_length=800, blank=True,null=True)

class learningsnowboarding(models.Model):
    title= models.CharField(max_length=200, unique=True)
    videos= models.ForeignKey(video)
    similar= models.ForeignKey("self", null=True, blank=True)
    descripton= models.TextField(max_length=800,  blank=True,null=True)
