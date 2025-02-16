from django.db import models
from apiazure.Modelo.Notify import Notify
from apiazure.Modelo.Organization import Organization
from apiazure.models import User

from django.db.models import UniqueConstraint

class Follow(models.Model):

    organizator = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["organizator", "user"], name="unique_follow")
        ]

