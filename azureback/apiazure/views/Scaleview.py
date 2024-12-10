from rest_framework.views import APIView
from apiazure.Modelo.Scale import Scale
from apiazure.Seralizer.Scaleseralizer import ScaleSeralizer
from rest_framework.response import Response
from apiazure.models import User
from apiazure.Modelo.Voluntary import Voluntary
import rest_framework.status  as status
from apiazure.Modelo.Horario import Horary
import rest_framework.permissions as permission

class ScaleDetailsList(APIView):
    
    permission_classes=[permission.AllowAny]
    
    def get(self,request,eventid):
        scale=Scale.objects.filter(id=eventid)
        scaleseralizer=ScaleSeralizer(scale,many=True)
        print(scaleseralizer.data)
        return Response(data=scaleseralizer.data,status=status.HTTP_200_OK)
    

class ScaleDetailsDelete(APIView):
    
    permission_classes=[permission.AllowAny]
    
    def post(self,request,horaryid,email):
        horary=Horary.objects.get(id=horaryid)
        user=User.objects.get(email=email)
        voluntary=Voluntary.objects.create(user=user)
        horary.max_voluntary_scale-=1
        horary.add_voluntary(voluntary=voluntary)
        horary.save()
        return Response(data={"msg":"entry voluntary"},status=status.HTTP_200_OK)