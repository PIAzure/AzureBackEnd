from rest_framework import serializers
from apiazure.models import User

class Userseralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ["email","name",
                 "password","isadmin",
                 "imagefield","isactive"]

        