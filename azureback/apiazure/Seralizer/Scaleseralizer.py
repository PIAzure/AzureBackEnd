from rest_framework import serializers
from apiazure.Modelo.Scale import Scale
from apiazure.Seralizer.HorarySeralizer import HorarySeralizer
class ScaleSeralizer(serializers.ModelSerializer):
    horarys=HorarySeralizer(many=True)
    class Meta:
        model=Scale
        fields=["id","event","horarys"]