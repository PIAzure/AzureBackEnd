from rest_framework import serializers
from apiazure.Modelo.Events import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields=["description",
                "location",
                "escale",
                "begin",
                "bscale",
                "banner",
                "organizator",
                "id",
                "end",
                "max_voluntary_per_horary",
                "max_particpant"]   
        # Inclui todos os campos no JSON da API


