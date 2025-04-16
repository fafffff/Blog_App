from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django_countries.fields import CountryField
import re
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
    address=forms.CharField(max_length=100,required=True)
    password=forms.CharField(widget=forms.PasswordInput,required=True)
    profile_picture=forms.ImageField(required=False)
    
    class Meta:
        model=CustomUser
        fields=('email','First_Name','username','Last_Name','phone_number','country',
                'profile_picture','gender','address','password','confirm_password','DoB')
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email address'}),
            'First_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}),
            'Last_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last Name'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your phone number'}),
            'country':CountrySelectWidget(attrs={'class':'form-control','placeholder':'Select your country'}),
            'profile_picture':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Upload your profile picture'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}),
            'confirm_password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm your password'}),
            'DoB':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter your date of birth'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
            
            
          
        }
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                raise ValidationError("Email already exists.")
            return email
        def clean_username(self):
            username = self.cleaned_data.get('username')
            if CustomUser.objects.filter(username=username).exists():
                raise ValidationError("Username already exists.")
            return username
        def clean_phone_number(self):
            phone_number = self.cleaned_data.get('phone_number')
            if CustomUser.objects.filter(phone_number=phone_number).exists():
                raise ValidationError("Phone number already exists.")
            return phone_number
        def clean_password(self):
            password = self.cleaned_data.get('password')
            if len(password) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
            if not re.search(r'[A-Z]', password):
                raise ValidationError("Password must contain at least one uppercase letter.")
            if not re.search(r'[a-z]', password):
                raise ValidationError("Password must contain at least one lowercase letter.")
            if not re.search(r'[0-9]', password):
                raise ValidationError("Password must contain at least one digit.")
            if not re.search(r'[@$!%*?&]', password):
                raise ValidationError("Password must contain at least one special character.")
            if password in ['12345678', 'password', 'qwerty', 'abc123']:
                raise ValidationError("Password is too common.")
            if password == self.cleaned_data.get('username'):
                raise ValidationError("Password cannot be the same as username.")
            if password == self.cleaned_data.get('email'):
                raise ValidationError("Password cannot be the same as email.")
            if password == self.cleaned_data.get('phone_number'):
                raise ValidationError("Password cannot be the same as phone number.")
            if password == self.cleaned_data.get('First_Name'):
                raise ValidationError("Password cannot be the same as first name.")
            return password
        def clean_confirm_password(self):
            password = self.cleaned_data.get('password')
            confirm_password = self.cleaned_data.get('confirm_password')
            if password != confirm_password:
                raise ValidationError("Passwords do not match.")
            return confirm_password
        