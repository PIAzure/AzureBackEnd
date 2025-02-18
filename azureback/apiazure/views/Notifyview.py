from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apiazure.Seralizer.NotifySeralizer import NotifySeralizer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from apiazure.Modelo.Horario import Horary
from apiazure.Modelo.Notify import Notify
from apiazure.Modelo.Follows import Follow

class NotifyView(APIView):
    permission_classes=[AllowAny]

    def get(self,request,useremail):
        notifys=Follow.objects.filter(user=useremail)
        notifys_list=[]
        for i in  notifys:
            notifys_list.extend(i.notiys.all())
        serialized_notifys = NotifySeralizer(notifys_list, many=True).data
        return Response(data=serialized_notifys,status=HTTP_200_OK)