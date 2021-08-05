from django.db.models import fields
from student_app.models import  login, stu_details
from django import forms
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class stu_detail_form(forms.ModelForm):
    class Meta:
        model = stu_details
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder' : 'Enter your First Name'}),
            'last_name' : forms.TextInput(attrs={'placeholder' : 'Enter your Last Name'}),
            'DOB': forms.TextInput(attrs={'type':'date'}),
            'grade':forms.TextInput(attrs={'placeholder':'Enter your Grade'}),
            'address':forms.TextInput(attrs={'placeholder':'Enter your Address'}),
            'phone_no':forms.TextInput(attrs={'placeholder':'Enter your Phone Number'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter your E-mail'}),
            
        }
        fields = '__all__'
class login_form(forms.ModelForm):
    class Meta:
        model = login
        widgets={
            'username':forms.TextInput(attrs={'placeholder':"username"}),
            'password':forms.TextInput(attrs={'placeholder':'password','type':'password'})
        }
        fields = "__all__"
class register_form(UserCreationForm):
    class Meta:
        model = User
        
        fields = {
            'username',
            
            'email',
        }