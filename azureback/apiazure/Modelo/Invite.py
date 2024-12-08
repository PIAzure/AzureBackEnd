from django.db import models
from apiazure.Modelo.Events import Event
from apiazure.Modelo.Organization import Organization
from apiazure.models import User
class Invite(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)