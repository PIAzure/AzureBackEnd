from apiazure.Modelo.Events import Event
from django.db import models
from apiazure.models import User

class WaitParticipant(models.Model):

    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'event'], name='unique_user_event_wait')
        ]