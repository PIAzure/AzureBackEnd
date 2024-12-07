from rest_framework import serializers
from apiazure.Modelo.Participants import Participants
from apiazure.models import User
from apiazure.Seralizer.Eventsseralizer import EventSerializer
class ParticipantsSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model=Participants
        fields=["id","event","user"]
    
    