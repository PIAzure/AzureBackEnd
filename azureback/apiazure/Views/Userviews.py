from apiazure.Modelo.User import User
from apiazure.Seralizer.Userseralizer import Userseralizer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes, parser_classes
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_400_BAD_REQUEST

# Create your views here.
def _get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
@api_view(["POST"])
def post_user(request)->Response:
    user=Userseralizer(data=request.data)
    if user.is_valid():
        user.save()
    else:
        return Response(data={"msg":"Bad Resquest"},status=HTTP_400_BAD_REQUEST)
    return Response(data=user.data,status=HTTP_201_CREATED)


@api_view(["POST"])
def authuser(request):
    name=request.data.get("email")
    password=request.data.get("password")
    
    user=User.objects.get(pk=name)
    token=_get_tokens_for_user(user=user)
    
    userserelizer=Userseralizer(user)
    return Response(data={
        "Token":token,
        "user":userserelizer.data
    })
    

@api_view(["GET"])
def getalluser(request)-> Response:
    try:
        user=User.objects.all()
        users=Userseralizer(user,many=True)
        return Response(data=users.data,status=HTTP_200_OK)
    except:
        return Response(data=[],status=HTTP_400_BAD_REQUEST)
    
@api_view(["PATCH","GET","DELETE","PUT"])
def getupdateuser(request,primary_key):
    if request.method=="PACTH":
        pass
    if request.method=="PUT":
        pass
    elif request.method=="GET":
        try:
            user=User.objects.get(pk=primary_key)
            userseralizer=Userseralizer(user)
            return Response(data=userseralizer.data,status=HTTP_200_OK)
        except:
            return Response(data={"msg":"not found user"},status=HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        try:
            user=User.objects.get(pk=primary_key)
            userseralizer=Userseralizer(user)
            user.delete()
            return Response(data=userseralizer.data,status=HTTP_200_OK)
        except:
            return Response(data={"msg":"not delete user"},status=HTTP_200_OK)
            
            