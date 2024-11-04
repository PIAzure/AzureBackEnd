from rest_framework import serializers
from apiazure.Modelo.User import User

class Userseralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= "__all__"
        