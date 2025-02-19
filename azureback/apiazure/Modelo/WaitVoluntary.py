from django.db import models
from apiazure.Modelo.Voluntary import Voluntary

class WaitVoluntary(models.Model):
    position=models.PositiveIntegerField()
    participant=models.ForeignKey(Voluntary,primary_key=True)