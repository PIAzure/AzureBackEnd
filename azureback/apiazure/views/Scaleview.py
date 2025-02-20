from rest_framework.views import APIView
from apiazure.Modelo.Scale import Scale
from apiazure.Seralizer.Scaleseralizer import ScaleSeralizer
from rest_framework.response import Response
from apiazure.models import User
from apiazure.Modelo.Voluntary import Voluntary
from apiazure.Seralizer.VoluntarySeralizer import VoluntarySeralizer
from apiazure.Seralizer.WaitVoluntarySeralizer import WaitVoluntarySeralizer
import rest_framework.status  as status
from apiazure.Modelo.Horario import Horary
from datetime import datetime
from apiazure.Modelo.WaitVoluntary import WaitVoluntary
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

class WaitEntryHorary(APIView):
    permission_classes=[permission.AllowAny]
    def post(self,request,horaryid):
        query=WaitVoluntary.objects.filter(scale=horaryid)
        voluntary=query.first()
        horary=Horary.objects.get(id=horaryid)
        if horary.max_voluntary_scale==0:
            return Response(data={"msg":"horary full"},status=status.HTTP_400_BAD_REQUEST)
        else:
            voluntary=Voluntary.objects.create(user=voluntary.user)
            voluntary.save()
            horary.add_voluntary(voluntary=voluntary)
            horary.save()
            return Response(data={"msg":"new voluntary"})        
class ScaleEntryWait(APIView):
    permission_classes=[permission.AllowAny]
    def get(self,request,email,horaryid):
        query=WaitVoluntary.objects.filter(scale=horaryid)
        print(query)
        count=1
        for i in query.iterator():
            if i.user.email==email:
                return Response(data={"msg":count},status=status.HTTP_200_OK)        
            count+=1
        return Response(data={"msg":-1},status=status.HTTP_400_BAD_REQUEST)
        
        
class ScaleDetailsDelete(APIView):
    
    permission_classes=[permission.AllowAny]
    def delete(self,request,horaryid,id):
        voluntary=Voluntary.objects.get(id=id)
        voluntary.delete()
        return Response(data={"msg":"leave horary"})
    
    def post(self,request,horaryid,email):
        horary=Horary.objects.get(id=horaryid)
        user=User.objects.get(email=email)
        voluntary=Voluntary.objects.create(user=user)
        if horary.max_voluntary_scale>0:
            horary.max_voluntary_scale-=1
            horary.add_voluntary(voluntary=voluntary)
            horary.save()
        else:
            dictwait={"user":email,"scale":horaryid}
            waitvoluntary=WaitVoluntarySeralizer(data=dictwait)
            if waitvoluntary.is_valid():
                waitvoluntary.save()
                return Response(data={"msg":"entry wait queue voluntary"})
            else:
                return Response(data=waitvoluntary.error_messages)
        return Response(data={"msg":"entry voluntary"},status=status.HTTP_200_OK)