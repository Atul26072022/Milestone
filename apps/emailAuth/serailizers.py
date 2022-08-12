from unicodedata import name
from rest_framework import serializers
from .models import userdata

class userdataSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    email= serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    # token = serializers.CharField(max_length=150)
    # verify = serializers.BooleanField(default=False)
    
    def create(self, validated_data):
        return userdata.objects.create(**validated_data)