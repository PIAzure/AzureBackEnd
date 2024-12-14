from django.db import models
from apiazure.models import User
from apiazure.Modelo.Events import Event
from apiazure.Modelo.Horario import Horary
class Scale(models.Model):
    id=models.AutoField(primary_key=True)
    event=models.OneToOneField(Event,unique=True,on_delete=models.CASCADE)
    horarys=models.ManyToManyField(Horary,related_name="horaryvoluntary",db_index=True)
        
    
        