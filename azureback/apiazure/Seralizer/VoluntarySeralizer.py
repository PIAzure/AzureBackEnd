
from rest_framework import serializers
from apiazure.Modelo.Voluntary import Voluntary
from apiazure.Seralizer.Userseralizer import Userseralizer

class VoluntarySeralizer(serializers.ModelSerializer):
    user=Userseralizer()
    class Meta:
        model=Voluntary
        fields=["user","id"]