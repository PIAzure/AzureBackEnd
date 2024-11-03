from apiazure.Modelo.User import User
from apiazure.Seralizer.Userseralizer import Userseralizer
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
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
def getalluser(request):
    pass

@api_view(["UPDATE","GET","DELETE"])
def getupdateuser():
    pass