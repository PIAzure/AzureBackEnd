from django.db import models

class Event(models.Model):
    timeDate= models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='banners/')  # Especifica o diretório para salvar as imagens

    def __str__(self):
        return f"{self.descricao} - {self.horarioedata}"
