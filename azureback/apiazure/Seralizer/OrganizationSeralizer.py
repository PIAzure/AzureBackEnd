from rest_framework import serializers
from apiazure.Modelo.Organization import Organization
from apiazure.Seralizer.Userseralizer import Userseralizer
class OrganizationSeralizer(serializers.ModelSerializer):
    users=Userseralizer(source="user",read_only=True)
    class Meta:
        model=Organization
        fields=["users","count","user"]
        extra_kwargs = {'user': {'write_only': True}}
        read_only=["users"]
        