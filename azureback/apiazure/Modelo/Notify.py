from django.db import models
from apiazure.Modelo.Organization import Organization
from apiazure.models import User

class Notify(models.Model):
    id=models.BigAutoField(primary_key=True)
    msg=models.TextField(max_length=10000)
    
