from rest_framework import serializers
from apiazure.Modelo.Events import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Inclui todos os campos no JSON da API


