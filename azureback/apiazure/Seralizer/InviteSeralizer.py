from rest_framework import serializers
from apiazure.Modelo.Invite import Invite
class InviteSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model=Invite
        fields=["id",
                "user",
                "event",]
        