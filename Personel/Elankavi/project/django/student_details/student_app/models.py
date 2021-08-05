from typing import ChainMap
from django.db import models
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, DateField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
choice=(
    ('Male','Male'),
    ('Female','Female'),
    ('others','others')
)
class stu_details(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade =models. CharField(max_length=10)
    DOB = models.DateField()
    gender = models.CharField(max_length=100 , choices=choice)
    email = models.EmailField(max_length=200,null=True)
    address = models.CharField(max_length=255)
    phone_no = PhoneNumberField(null=True,blank=True)
    image=models.ImageField(upload_to="uploads/%Y/%m/%D/",null=True , blank = True)

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)




