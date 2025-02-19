from rest_framework import serializers
from apiazure.Modelo.Voluntary import Voluntary
class WaitVoluntarySeralizer(serializers.ModelSerializer):
    
    class Meta:
        model=Voluntary
        fields="__all__"