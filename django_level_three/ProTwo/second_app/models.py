
 
from django.db import models
from django import forms
#from django.core import validators
from django.db.models import fields




# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    user_mail = models.CharField(max_length=250,unique= True)
"""
    verify_email = forms.EmailField(label='Type email again:')
    age = forms.IntegerField(max_value=60)
    comments = forms.CharField(widget=forms.Textarea)
"""