
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=250,primary_key=True)
    password=models.CharField(max_length=100)
    isadmin=models.BooleanField(default=False)
    imagefield=models.ImageField(upload_to="images/",default=None)
    
    
