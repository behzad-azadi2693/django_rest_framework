from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import (
        ModelSerializer,HyperlinkedIdentityField, SerializerMethodField,
        ValidationError
    )



class UserCreateSerializer(ModelSerializer):
    email2 = serializers.EmailField(label='confirm email')
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'email2']
        extra_kwargs = {
            'password':{
                'write_only':True,
            }
        }
    
    def validate(self, data):
        email = data['email']
        user = User.objects.filter(email = email)
        if user:
            raise ValidationError("this user has already register")
        return data
         
    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get['email']
        email12 = value
        if email1 != email12:
            raise ValidationError('email must match')
        return value
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
        

