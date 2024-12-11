from django.db import models
from apiazure.models import User

class Voluntary(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="uservoluntary")