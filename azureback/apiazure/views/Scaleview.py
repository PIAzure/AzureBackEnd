from rest_framework.views import APIView
from apiazure.Modelo.Scale import Scale
from apiazure.Seralizer.Scaleseralizer import ScaleSeralizer
from rest_framework.response import Response
from apiazure.models import User
from apiazure.Modelo.Voluntary import Voluntary
import rest_framework.status  as status
from apiazure.Modelo.Horario import Horary
from datetime import datetime
import rest_framework.permissions as permission

class ScaleDetailsList(APIView):
    
    permission_classes=[permission.AllowAny]
    
    
    def get(self,request,id):
        scale=Scale.objects.filter(id=id)
        scaleseralizer=ScaleSeralizer(scale,many=True)
        copy=scaleseralizer.data.copy()
        for horary in copy:
            horary["horarys"]=sorted(horary["horarys"],key=lambda x:datetime.strptime(x["datetime"], "%Y-%m-%dT%H:%M:%SZ"))
        return Response(data=copy,status=status.HTTP_200_OK)
    
class ScaleDetailVoluntary(APIView):
    permission_classes=[permission.AllowAny]
    
    def delete(self,request,horaryid,voluntaryid):
        voluntary=Voluntary.objects.get(id=voluntaryid)
        horary=Horary.objects.get(id=horaryid)
        horary.max_voluntary_scale+=1
        horary.save()
        voluntary.delete()
        return Response(data={"msg":"leave horary"})
class ScaleDetailsDelete(APIView):
    
    permission_classes=[permission.AllowAny]
    def delete(self,request,horaryid,id):
        voluntary=Voluntary.objects.get(id=id)
        voluntary.delete()
        return Response(data={"msg":"leave horary"})
    
    def post(self,request,horaryid,email):
        horary=Horary.objects.get(id=horaryid)
        user=User.objects.get(email=email)
        voluntary=Voluntary.objects.create(user=user,)
        horary.max_voluntary_scale-=1
        horary.add_voluntary(voluntary=voluntary)
        horary.save()
        return Response(data={"msg":"entry voluntary"},status=status.HTTP_200_OK)