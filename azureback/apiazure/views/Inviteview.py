from rest_framework.views import APIView
from apiazure.Modelo.Events import Event
from apiazure.Seralizer.InviteSeralizer import InviteSeralizer
from apiazure.Modelo.Invite import Invite
from rest_framework.response import Response
import rest_framework.status  as status
from apiazure.Modelo.Participants  import Participants

import rest_framework.permissions as permission
class InviteDetailsPost(APIView):
    permission_classes=[permission.AllowAny]
    def post(self,request):
        copy=request.data.copy()
        inviteseralizer=InviteSeralizer(data=copy)
        event=Event.objects.get(id=copy["event"])
        if event.max_particpant==0 or not inviteseralizer.is_valid():
            return Response(data={"msg":"error invite"})
        inviteseralizer.save()
        return Response(data=inviteseralizer.data,status=status.HTTP_201_CREATED)

class InviteDetailList(APIView):
    permission_classes=[permission.AllowAny]
    def get(self,request,email):
        invite=Invite.objects.filter(user=email,)
        inviteseralizer=InviteSeralizer(invite,many=True)
        return Response(data=inviteseralizer.data,status=status.HTTP_200_OK)
    
class InviteDetatailAceptRecuse(APIView):
    
    permission_classes=[permission.AllowAny]
    
    def delete(self,request,idinvite):
        invite=Invite.objects.get(id=idinvite)
        invite.delete()
        return Response(data={"msg":"recuse invite"},status=status.HTTP_200_OK)
    
    def post(self, request, idinvite):
        
        invite = Invite.objects.get(id=idinvite)

        Participants.objects.create(event=invite.event, user=invite.user)

        invite.delete()

        event = invite.event  # Use o objeto diretamente
        event.max_particpant -= 1
        event.save()


        return Response(data={"msg": "invite accepted"}, status=status.HTTP_200_OK)
