from apiazure.Modelo.User import User
from apiazure.Seralizer.Userseralizer import Userseralizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_400_BAD_REQUEST

# Create your views here.

@api_view(["POST"])
def post_user(request)->Response:
    user=Userseralizer(data=request.data)
    if user.is_valid():
        user.save()
    else:
        return Response(data={"msg":"BAD REQUEST"},status=HTTP_400_BAD_REQUEST)
    return Response(data=user.data,status=HTTP_201_CREATED)

@api_view(["GET"])
def getalluser(request)-> Response:
    try:
        user=User.objects.all()
        users=Userseralizer(user,many=True)
        return Response(data=users.data,status=HTTP_200_OK)
    except:
        return Response(data=[],status=HTTP_400_BAD_REQUEST)
    
@api_view(["UPDATE","GET","DELETE"])
def getupdateuser(request,pk):
    if request.method=="UPDATE":
        pass
    elif request.method=="GET":
        try:
            user=User.objects.get(pk)
            userseralizer=Userseralizer(user)
            return Response(data=userseralizer.data,status=HTTP_200_OK)
        except:
            return Response(data={"msg":"not found user"},status=HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        try:
            user=User.objects.get(id=pk)
            userseralizer=Userseralizer(user)
            user.delete()
            return Response(data=userseralizer.data,status=HTTP_200_OK)
        except:
            return Response(data={"msg":"not delete user"},status=HTTP_200_OK)
            
            