from django import forms
from django.db.models import fields
from django.forms import widgets
from quiz_app.models import login_model
from quiz_app.models import *

class login_form(forms.ModelForm):
    class Meta:
        model = login_model
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'username'}),
            'password' : forms.TextInput(attrs={'placeholder' : 'password','type':'password'}),
        }
        fields = '__all__'
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields={
            'username',
            'email',
            
        }
    def save(self, commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.username=self.cleaned_data['username']
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class pythonform(forms.ModelForm):
    class Meta:
        model=python
        fields="__all__"

class linuxform(forms.ModelForm):
    class Meta:
        model=linux
        fields="__all__"
class gitform(forms.ModelForm):
    class Meta:
        model=git
        fields="__all__"
