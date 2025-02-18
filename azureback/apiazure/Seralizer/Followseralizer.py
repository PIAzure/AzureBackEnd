from apiazure.Modelo.Follows import Follow
from rest_framework import serializers

from apiazure.Seralizer.NotifySeralizer import NotifySeralizer

class FollowSeralizer(serializers.ModelSerializer):
    notiys=NotifySeralizer(read_only=True,many=True)
    class Meta:
        model=Follow
        fields=["id","user",
                "organizator","notiys"]

        

