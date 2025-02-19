from rest_framework.views import APIView
from apiazure.Modelo.Events import Event
from rest_framework.response import Response
import rest_framework.status as status
import rest_framework.permissions as permissions
from apiazure.Modelo.Participants import Participants
from apiazure.models import User
from apiazure.Seralizer.ParticipantsSeralizer import ParticipantsSeralizer
from apiazure.Seralizer.WaitParticipantSeralizer import WaitParticipantSeralizer
from apiazure.Modelo.WaitParticipants import WaitParticipant

class ParticipantsDetailsGet(APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def get(self,request,eventid):
        participants=Participants.objects.filter(event=eventid)
        participantsseralizer=ParticipantsSeralizer(participants,many=True)
        return Response(data=participantsseralizer.data,status=status.HTTP_200_OK)
class WaitParticipantDetail(APIView):
    
    permission_classes=[permissions.AllowAny]

    def get(self,request,eventid):
        waitparticipant=WaitParticipant.objects.filter(event=eventid)
        waitseralizer=WaitParticipantSeralizer(waitparticipant,many=True)
        return Response(data=waitseralizer.data,status=status.HTTP_200_OK)
    

    def post(self, request, eventid):
        
        wait_participant = WaitParticipant.objects.filter(event=eventid).first()
        if not wait_participant:
            return Response(data={"msg": "No participants in the waiting list"}, status=400)
        event = Event.objects.filter(id=eventid).first()
        if not event:
            return Response(data={"msg": "Event not found"}, status=404)

        if event.max_particpant==0:
            return Response(data={"msg": "Event is already full"}, status=400)

        participant_data = {
            "user": wait_participant.user.email,
            "event": wait_participant.event.id
        }

        participant_serializer = ParticipantsSeralizer(data=participant_data)
        if participant_serializer.is_valid():
                wait_participant.delete()
                participant_serializer.save()
                return Response(data={"msg": "First participant entry"}, status=201)

        return Response(data={"msg": "Error saving participant", "errors": participant_serializer.errors}, status=400)

class ParticipantsDetailsDelete(APIView):
    
    permission_classes=[permissions.AllowAny]
        
    def delete(self,request,id_participant):   
        participant=Participants.objects.get(id=id_participant)
        event=Event.objects.get(id=participant.event.id)
        if event.max_particpant>=0:
            participant.delete()
            event.max_particpant+=1
            event.save()
        return Response(data={"msg":"leave event"})
    
class ParticipantDetailGetEmail(APIView):
    permission_classes=[permissions.AllowAny]
    
    def get(self,request,email):
        user=User.objects.get(email=email)
        participants=Participants.objects.filter(user=user)
        participantsseralizer=ParticipantsSeralizer(participants,many=True)
        return Response(data=participantsseralizer.data,status=status.HTTP_200_OK)
class ParticipantsDetailsPost(APIView):
    
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        copy=request.data.copy()
        participant=ParticipantsSeralizer(data=copy)
        event=Event.objects.get(id=copy["event"])
        if not participant.is_valid(): 
            return Response(data=participant.errors,status=status.HTTP_400_BAD_REQUEST)
        if event.max_particpant>0 and participant.is_valid():
            print("cadastrou o participant no evento")
            participant.save()
            event.max_particpant-=1
            event.save()
            return Response(data={"msg":"participant entry event"},status=status.HTTP_400_BAD_REQUEST)
        else:
            print("lista de espera")
            waitparticipant=WaitParticipantSeralizer(data=copy) 
            if waitparticipant.is_valid():
                waitparticipant.save()
                return Response(data=waitparticipant.data,status=status.HTTP_200_OK)
            return Response(data=participant.error_messages,status=status.HTTP_200_OK)