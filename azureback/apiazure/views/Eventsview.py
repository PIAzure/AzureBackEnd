from apiazure.Modelo.Events import Event
from apiazure.Seralizer.Eventsseralizer import EventSerializer
from apiazure.Modelo.Organization import Organization
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from datetime import datetime , timedelta
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from apiazure.Modelo.Scale import Scale
from apiazure.Modelo.Horario import Horary
class EventDetailListPost(APIView):
    
    permission_classes=[AllowAny]
    def __create_scale_none(self,event:Event):
        begindatetime:datetime=datetime.strptime(event.begin.isoformat().replace('+00:00', 'Z'),"%Y-%m-%dT%H:%M:%SZ")
        enddatetieme:datetime=datetime.strptime(event.end.isoformat().replace('+00:00', 'Z'),"%Y-%m-%dT%H:%M:%SZ")
        scale=Scale.objects.create(event=event)
        while(begindatetime<enddatetieme):
            horary=Horary.objects.create(datetime=begindatetime.isoformat().replace('+00:00', 'Z'),max_voluntary_scale=event.max_voluntary_per_horary)
            scale.horarys.add(horary)
            begindatetime+=timedelta(hours=1)
        scale.save()
    
    def post(self,request) -> Response:
        copy=request.data.copy()
        event = EventSerializer(data=request.data)
        
        if event.is_valid():
            event.save()
            eventid=event.data["id"]
            organization=Organization.objects.get(user_id=copy["organizator"])
            organization.count+=1
            organization.save()
            eventquery=Event.objects.get(id=eventid)
            self.__create_scale_none(event=eventquery)
            return Response(data=event.data, status=HTTP_201_CREATED)
        else:
            return Response(data={"msg": "BAD REQUEST"}, status=HTTP_400_BAD_REQUEST)

class EventDetailListGet(APIView):
        
    permission_classes=[AllowAny]
    
    def get(self,request,email) -> Response:
        events = Event.objects.filter(organizator_id=email)
        events_serializer = EventSerializer(events, many=True)
        return Response(data=events_serializer.data, status=HTTP_200_OK)
        
class EventAdminDetail(APIView):
    
    permission_classes=[AllowAny]
    
    def get(self,request) -> Response:
        events = Event.objects.all()
        events_serializer = EventSerializer(events, many=True)
        return Response(data=events_serializer.data, status=HTTP_200_OK)

class EventDetail(APIView):
    
    permission_classes=[AllowAny]
    
    def _get_object(self,primary_key)->(Event|Response):
        try:
            event = Event.objects.get(pk=primary_key)
            return event
        except Event.DoesNotExist:
            return Response(data={"msg": "Event not found"}, status=HTTP_400_BAD_REQUEST)
        
    def get(self,request,primary_key):
        event=self._get_object(primary_key=primary_key)
        event_serializer = EventSerializer(event)
        return Response(data=event_serializer.data, status=HTTP_200_OK)
    
    def delete(self, request, primary_key):
        event=self._get_object(primary_key=primary_key)
        event.delete()
        return Response(data={"msg": "Event deleted successfully"}, status=HTTP_200_OK)
    
    def put(self,request,primary_key):
            event=self._get_object(primary_key=primary_key)
            event_serializer = EventSerializer(event, data=request.data)
            if event_serializer.is_valid():
                event_serializer.save()
                return Response(data=event_serializer.data, status=HTTP_200_OK)
            else:
                return Response(data={"msg": "BAD REQUEST"}, status=HTTP_400_BAD_REQUEST)
       
            
            






