from rest_framework.views import APIView
from apiazure.Modelo.Events import Event
from apiazure.Seralizer.InviteSeralizer import InviteSeralizer
from apiazure.Modelo.Invite import Invite
from rest_framework.response import Response
import rest_framework.status  as status
from apiazure.Modelo.Participants  import Participants
import rest_framework.permissions as permission

class ScaleDetailsList(APIView):
    
    def get(self,eventid):
        p