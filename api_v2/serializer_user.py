from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password':{
                'write_only':True,
            }
        }
    
    def validate(self, data):
        email = data.get('email')
        user = User.objects.filter(email = email)
        if user:
            raise ValidationError("this user has already register")
        return data


class UserLoginSerializer(ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(label='Email address', required=False,allow_blank=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'tocken']
        extra_kwargs={
            'password':{
                'write_only':True,
            }
        }
    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not emial and not username:
            raise ValidationError('a username or email is reqiured to login')
        user = User.objects.filter(
            Q(username=username)|
            Q(email=email)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('this user/email is not validate')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('please try egain')
        return  data
