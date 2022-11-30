from ast import UAdd
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        extra_kwargs = {'password' : {'write_only':True,'required':True}}

    def create(self,validated_data):
        user = User.objects.create_user(validated_data)
        return user
