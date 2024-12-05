from django.db import models
from apiazure.models import User
from apiazure.Modelo.Events import Event
class Participants(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userspart")
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="eventpart")