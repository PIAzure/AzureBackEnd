from rest_framework import serializers
from apiazure.Modelo.Participants import Participants
from apiazure.models import User
from apiazure.Seralizer.Eventsseralizer import EventSerializer
class ParticipantsSeralizer(serializers.ModelSerializer):
    events=EventSerializer(read_only=True,source="event")
    class Meta:
        model=Participants
        fields=["id","event","user","events"]
        extra_kwargs = {'event': {'write_only': True}}
        read_only=["events"]
    
    