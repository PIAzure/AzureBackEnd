from rest_framework import serializers
from apiazure.Modelo.Participants import Participants
from apiazure.Seralizer import Userseralizer
from apiazure.Seralizer import Eventsseralizer
class ParticipantsSeralizer(serializers.ModelSerializer):
    events=Eventsseralizer(read_only=True,source="eventpart")
    users=Userseralizer(read_only=True,source="userspart")

    class Meta:
        model=Participants
        fields=["event","user"]
        extras_kwargs={"event":True,"user":True}
        read_only=["id","users","events"]