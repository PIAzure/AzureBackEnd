from django.db import models
from apiazure.Modelo.Organization import Organization

class Event(models.Model):
    id=models.AutoField(primary_key=True)
    organizator=models.ForeignKey(Organization,null=True,on_delete=models.CASCADE)
    max_particpant=models.PositiveIntegerField(default=10)
    max_voluntary_per_horary=models.PositiveIntegerField()
    begin= models.DateTimeField()
    end=models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='banners/') 

