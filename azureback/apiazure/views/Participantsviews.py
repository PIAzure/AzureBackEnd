from rest_framework.views import APIView
from apiazure.Modelo.Events import Event
from rest_framework.response import Response
import rest_framework.status as status
import rest_framework.permissions as permissions
from apiazure.Modelo.Participants import Participants
from apiazure.Seralizer.ParticipantsSeralizer import ParticipantsSeralizer

class ParticipantsDetailsGet(APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def get(self,request,eventid):
        participants=Participants.objects.filter(event=eventid)
        participantsseralizer=ParticipantsSeralizer(participants,many=True)
        return Response(data=participantsseralizer.data,status=status.HTTP_200_OK)

class ParticipantsDetailsDelete(APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def delete(self,request,id_participant):   
        participant=Participants.objects.get(id=id_participant)
        participant.delete()
        event=Event.objects.get(id=participant.id)
        event.max_particpant+=1
        event.save()
        return Response(data={"msg":"leave event"})
    
class ParticipantsDetailsPost(APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def post(self,request):
        copy=request.data.copy()
        participant=ParticipantsSeralizer(data=copy)
        event=Event.objects.get(id=copy["event"])
        print(participant.is_valid())
        if not participant.is_valid(): 
            return Response(data=participant.errors,status=status.HTTP_400_BAD_REQUEST)
        participant.save()
        event.max_particpant-=1
        event.save()
        return Response(data=participant.data,status=status.HTTP_200_OK)