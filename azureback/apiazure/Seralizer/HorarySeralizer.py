from rest_framework import serializers
from apiazure.Modelo.Scale import Horary
from apiazure.Seralizer.VoluntarySeralizer import VoluntarySeralizer
class HorarySeralizer(serializers.ModelSerializer):
    voluntarys=VoluntarySeralizer(many=True)
    class Meta:
        model=Horary
        fields=["id","datetime","voluntarys","max_voluntary_scale"]
