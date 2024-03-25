from django import forms
from .models import Package
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput,TextInput



#Create User

class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields=['first_name','last_name','username','email','password1','password2']


#Authenticate User

class LoginForm(AuthenticationForm):
    class Meta:
        model =User
        fields=['username','password',]