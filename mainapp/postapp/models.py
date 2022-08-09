from distutils.command.upload import upload
from tkinter import Image
from tkinter.tix import Tree
from django.db import models
from django.forms import ImageField
from accountapp.models import User

# Create your models here.

class TimeStamp(models.Model):
    upload_dt = models.DateField(auto_now=True)
    edit_dt   = models.DateField(auto_now=True)

class Tweet(TimeStamp):
    owner     = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER')
    text      = models.CharField(max_length=2048)
    img       = models.ImageField(upload_to='images')