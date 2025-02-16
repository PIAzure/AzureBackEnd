from apiazure.Modelo.Follows import Follow
from rest_framework import serializers

class FollowSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model=Follow
        fields=["id","user","organizator"]

        

