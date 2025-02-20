from rest_framework import serializers
from apiazure.Modelo.WaitVoluntary import WaitVoluntary
class WaitVoluntarySeralizer(serializers.ModelSerializer):
    class Meta:
        model=WaitVoluntary
        fields="__all__"