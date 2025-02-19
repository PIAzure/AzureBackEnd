from rest_framework.views import APIView
import rest_framework.status  as Status
from rest_framework.permissions import AllowAny
from apiazure.Seralizer.OrganizationSeralizer import OrganizationSeralizer 
from apiazure.Seralizer.Userseralizer import Userseralizer
from rest_framework.response import Response
from apiazure.Modelo.Organization import Organization
from apiazure.utils import passwordcryptgraf
class OrganizationListView(APIView):
    
    """
        Retrive Create Organization
    """
    
    permission_classes=[AllowAny]
    def post(self,request):
        data=request.data.copy()
        data["isactive"]=True
        userseralizer=Userseralizer(data=data)
        if userseralizer.is_valid():
            userseralizer.save()
        data={"user":userseralizer.data["email"],"count":0}
        organizationseralizer=OrganizationSeralizer(data=data)
        
        if organizationseralizer.is_valid():
            organizationseralizer.save()
        return Response(data={"user":userseralizer.data,"count":0},status=Status.HTTP_201_CREATED)
    
    def get(self,request):
        organization=Organization.objects.all().intersection()
        organizationall=OrganizationSeralizer(organization,many=True)
        copy=organizationall.data.copy()
        for i in copy:
            i["users"]["password"]=passwordcryptgraf(i["users"]["password"])
        return Response(data=organizationall.data,status=Status.HTTP_200_OK)
    

class OrganizationViewDetail(APIView):
    """
        get instance user
    """
    permission_classes=[AllowAny]
    
    def get(self,request,primary_key)->Response:
        organization=Organization.objects.get(pk=primary_key)
        organizationseralizer=OrganizationSeralizer(organization)
        if organizationseralizer.data["users"]["isactive"]==False:
            return Response(data={"msg":"user not found"},status=Status.HTTP_404_NOT_FOUND)
        copy=organizationseralizer.data.copy()
        copy["users"]["password"]=passwordcryptgraf(copy["users"]["password"])
        return Response(data=organizationseralizer.data,status=Status.HTTP_200_OK)