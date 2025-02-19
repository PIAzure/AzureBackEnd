from rest_framework.serializers import serializers 
from apiazure.Modelo.Participants import Participants
class WaitParticipantSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Participants
        fields="__all__"