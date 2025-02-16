from rest_framework.views import APIView
from apiazure.Modelo.Events import Event
from rest_framework.permissions import AllowAny
from apiazure.Seralizer.Followseralizer import FollowSeralizer
from apiazure.Modelo.Follows import Follow
from rest_framework.response import Response
import rest_framework.status  as status

class FollowPost(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        print(request.data)
        followseralizer=FollowSeralizer(data=request.data)
        if followseralizer.is_valid():
            followseralizer.save()
            print("save")
            return Response(data={"msg":followseralizer.data["user"]+"follow:"+followseralizer.data["organizator"]},status=status.HTTP_201_CREATED)
        print("error")
        return Response(data=followseralizer.error_messages)

class FollowDelete(APIView):
    permission_classes=[AllowAny]
    def delete(self,request,followid):
        follow=Follow.objects.get(id=followid)
        unfollow=follow.delete()
        print(unfollow)
        return Response(data={"msg":f"unfollow {unfollow}"})
    
    def get(self,request,email):
        follow=Follow.objects.filter(organizator=email)
        followseralizer=FollowSeralizer(follow,many=True)
        return Response(data=followseralizer.data,status=status.HTTP_201_CREATED)