from django.db import models
from apiazure.Modelo.Participants import Participant

class WaitParticipant(models.Model):
    posision=models.AutoField(primary_key=True)
    participant=models.ForeignKey(Participant)