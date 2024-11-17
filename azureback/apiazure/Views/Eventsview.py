from rest_framework import viewsets
from apiazure.Modelo.Events import Event
from apiazure.Seralizer.Eventsseralizer import EventSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
