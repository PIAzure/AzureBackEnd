from django.db import models
from apiazure.Modelo.Voluntary import Voluntary
class Horary(models.Model):
    id=models.AutoField(primary_key=True)
    max_voluntary_scale=models.PositiveBigIntegerField()
    datetime=models.DateTimeField()
    voluntarys=models.ManyToManyField(Voluntary,related_name="voluntarylist")
    
    def add_voluntary(self, voluntary):
        if self.max_voluntary_scale==-1:
            raise ValueError("Escala cheia")
        self.voluntarys.add(voluntary)