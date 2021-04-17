from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
#class LogIn(models.Model):

class Customer(models.Model):
    Username = models.CharField(max_length= 40)
    Email = models.EmailField(max_length = 15)
    Password = models.CharField(max_length=10)

    def register(self):
        self.save()


class LogIn(models.Model):
    Username = models.CharField(max_length= 40)
    Password = models.CharField(max_length=50, default="", editable=False)

   
