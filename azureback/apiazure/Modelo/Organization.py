from django.db import models
from apiazure.models import User

class Organization(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="user")
    count=models.IntegerField(default=0)
