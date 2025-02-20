from django.db import models
from apiazure.Modelo.Horario import Horary
from apiazure.models import User

class WaitVoluntary(models.Model):
    id=models.AutoField(primary_key=True)
    scale=models.ForeignKey(Horary,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="waitvoluntary")