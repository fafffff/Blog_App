from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin,Group,Permission
import uuid
from django_countries.fields import CountryField
class CustomUserManager(BaseUserManager):
   def create_user(self, email, password=None, **extra_fields):
       if not email:
           raise ValueError('The Email field must be set')
       email=self.normalize_email(email)
       user=self.model(email=email, **extra_fields)
       user.set_password(password)
       user.save()
       return user
       
   def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superAdmin', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superAdmin') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

Gender_choices=[
    ('male',"Male"),
    ('female',"Female"),
    ('other',"Other"),
]

class CustomUser(models.Model):
    Id=models.UUIDField(primary_key=True, 
                        editable=False,unique=True,default=uuid.uuid4)
    
    user_Name=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True,max_length=100)
    password=models.CharField(max_length=100,required=True)
    First_Name=models.CharField(max_length=100,blank=True,null=True,)
    Last_Name=models.CharField(max_length=100,blank=True,null=True)
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    DoB=models.DateField(blank=True,null=True)
    gender=models.CharField(max_length=10,choices=Gender_choices,
                            default='Female',blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    country=CountryField(blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profile_pictures',blank=True,null=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superAdmin=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    groups=models.ManyToManyField(
        Group,
        related_name='custom_user_group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions=models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )
    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_Name','First_Name','Last_Name']
    
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}-{self.email}"

          