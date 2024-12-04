from apiazure.models import User
from apiazure.Seralizer.Userseralizer import Userseralizer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Dict
from rest_framework.views import APIView 
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_400_BAD_REQUEST


class UserDetail(APIView):
    
    def get(self,request,primary_key):
        try:
            user=User.objects.get(pk=primary_key)
            if user.isactive==False: 
                raise Exception
            userseralizer=Userseralizer(user)
            return Response(data=userseralizer.data,status=HTTP_200_OK)
        except:
            return Response(data={"msg":"not found user"},status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,primary_key):
        try:
            user=User.objects.get(pk=primary_key)
            userseralizer=Userseralizer(user,data={"isactive":False},partial=True)
            if userseralizer.is_valid():
                userseralizer.save()
                return Response(data={"msg":"delete user"},status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data={"msg":"not delete user"},status=HTTP_200_OK)
    
    def put(self,request,primary_key):
        user=User.objects.get(pk=primary_key)
        data = request.data.copy()
        files = request.FILES  # Images and other binary files

        if "imagefield" in files:
            data["imagefield"] = files["imagefield"]
    
        user_serializer = Userseralizer(user, data=data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
        return Response(data=user_serializer.data,status=HTTP_200_OK)

class UserAdminDetail(APIView):
    
    permission_classes=[AllowAny]

    
    def __tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def post(self,request)->Response:
        
        name:str=request.data.get("email")
        password:str=request.data.get("password")
    
        user=User.objects.get(pk=name)
    
        if user.isactive==False:
            return Response(data={"msg":"user not found"})
        
        if user.password!=password:
            return Response(data={"msg":"not match password"},status=HTTP_400_BAD_REQUEST)
    
        token=self.__tokens_for_user(user=user)
    
        userserelizer:Userseralizer=Userseralizer(user)
        return Response(data={"Token":token,"user":userserelizer.data})
    
class UserListDetail(APIView):
    
    permission_classes=[AllowAny]
    
    def post(self,request)->Response:
        data=request.data.copy()
        data["isactive"]=True
        user:Userseralizer=Userseralizer(data=data)
        if user.is_valid():
            user.save()
        else:
            return Response(data={"msg":"Bad Resquest"},status=HTTP_400_BAD_REQUEST)
        return Response(data=user.data,status=HTTP_201_CREATED)

    def get(self,request)-> Response:
        try:
            user=User.objects.all().filter(isactive=True)
            users=Userseralizer(user,many=True)
            return Response(data=users.data,status=HTTP_200_OK)
        except:
            return Response(data=[],status=HTTP_400_BAD_REQUEST)
    

            
            