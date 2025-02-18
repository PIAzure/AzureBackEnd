from apiazure.Modelo.Notify import Notify
from rest_framework import serializers

class NotifySeralizer(serializers.ModelSerializer):
    
    class Meta:
        model=Notify
        fields="__all__"