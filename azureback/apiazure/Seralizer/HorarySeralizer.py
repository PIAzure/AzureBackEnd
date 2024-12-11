from rest_framework import serializers
from apiazure.Modelo.Scale import Horary
from apiazure.Seralizer.VoluntarySeralizer import VoluntarySeralizer
class HorarySeralizer(serializers.ModelSerializer):
    
    voluntary=VoluntarySeralizer(source="uservoluntary",read_only=True)
    
    class Meta:
        model=Horary
        fields=["id",
                "event",
                "horarys"]
        read_only=["voluntary"]