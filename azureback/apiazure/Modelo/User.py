from django.db import models

class User(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=250,primary_key=True)
    password=models.CharField(max_length=100)
    imagefield=models.ImageField(upload_to="images/",default=None)
    
