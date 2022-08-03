import email
from lib2to3.pgen2 import token
from unicodedata import name
from django.db import models

# Create your models here.
class userdata(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=150)
    verify = models.BooleanField(default=False)
