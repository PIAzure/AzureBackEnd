from django.db import models
from apiazure.Modelo.Organization import Organization

class Event(models.Model):
    organizator=models.ForeignKey(Organization)
    timeDate= models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='banners/')  # Especifica o diretório para salvar as imagens

    def __str__(self):
        return f"{self.descricao} - {self.horarioedata}"
