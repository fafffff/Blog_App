from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django_countries.fields import CountryField

class UserRegistration():
    email=forms.EmailField(
        max_length=100,help_text=' use a valid email address.'
    )
    First_Name=forms.CharField(max_length=100,required=True)
    Last_Name=forms.CharField(max_length=100,required=True)
    phone_number=forms.CharField(max_length=15,required=True)
    country=CountryField(blank_label='Country').formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'}),
        required=True,
    )