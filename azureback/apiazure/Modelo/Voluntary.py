from django.db import models
from apiazure.models import User

class Voluntary(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="uservoluntary")