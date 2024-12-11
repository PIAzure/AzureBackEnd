
from rest_framework import serializers
from apiazure.Modelo.Voluntary import Voluntary
from apiazure.Seralizer.Userseralizer import Userseralizer

class VoluntarySeralizer(serializers.ModelSerializer):
    users=Userseralizer(source="uservoluntary",read_only=True)
    class Meta:
        model=Voluntary
        fields=["users","id"]