from django.db import models
from apiazure.Modelo.Voluntary import Voluntary
class Horary(models.Model):
    id=models.AutoField(primary_key=True)
    max_voluntary_scale=models.PositiveBigIntegerField()
    datetime=models.DateTimeField()
    voluntarys=models.ManyToManyField(Voluntary,related_name="voluntarylist")
    
    def add_voluntary(self, voluntary):
        """
        Adiciona um voluntário à lista se não ultrapassar o limite máximo.
        """
        if self.voluntarys.count() >= self.max_voluntary_scale:
            raise ValueError("O número máximo de voluntários para este horário já foi atingido.")
        self.voluntarys.add(voluntary)