from apiazure.Modelo.Events import Event
from apiazure.Seralizer.Eventsseralizer import EventSerializer
from apiazure.Modelo.Voluntary import Voluntary
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.permissions  as permissions 
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

class VoluntaryDetailsDelete(APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def delete(self,request,idvoluntary):   
        voluntary=Voluntary.objects.get(id=idvoluntary)
        voluntary.delete()
        return Response(data={"msg":"voluntary leave scale"})
    
class VoluntarysDetailsPost(APIView):
    
    permission_classes=[permissions.AllowAny]
    
    def post(self,request):
        pass