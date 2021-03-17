from django.contrib.auth.models import User
from rest_framework.serializers import (
        ModelSerializer,HyperlinkedIdentityField, SerializerMethodField,
        ValidationError
    )

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password':{
                'write_only':True,
            }
        }
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email = email 
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        

