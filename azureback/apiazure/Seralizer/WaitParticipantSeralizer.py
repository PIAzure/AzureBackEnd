from rest_framework import serializers 
from apiazure.Modelo.WaitParticipants import WaitParticipant
class WaitParticipantSeralizer(serializers.ModelSerializer):
    class Meta:
        model=WaitParticipant
        fields="__all__"