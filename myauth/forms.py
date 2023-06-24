from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"password1","password2"]

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

