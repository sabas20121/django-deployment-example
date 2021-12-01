
 
from django.db import models



# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    user_mail = models.CharField(max_length=250,unique= True)
