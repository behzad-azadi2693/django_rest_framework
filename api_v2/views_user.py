from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializer_user import UserSerializer


class UserDetail(APIView):
    def get(self, request, username):
        users = User.objects.get(username=username)
        srz = UserSerializer(instance=users).data
        return Response(srz, status=status.HTTP_200_OK)

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        srz = UserSerializer(instance=users, many=True).data
        return Response(srz, status=status.HTTP_200_OK)


class UserCreate(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        srz = UserSerializer(data=request.data)
        if srz.is_valid():
            srz.save()
            return Response(srz.data, status=status.HTTP_201_CREATED)
        return Response(srz.error, status=status.HTTP_400_BAD_REQUEST)      


class UserUpdate(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def put(self, request, username):
        user = User.opjects.get(username=username)
        self.check_permissions(request, user)
        srz = UserSerializer(instance=user, data=request.data, partial=True)
        if srz.is_valid():
            srz.save()
            return Response(srz.data, status= status.HTTP_200_OK)
        return Response(srz.error, status=status.HTTP_400_BAD_REQUEST)


class UserDelete(APIView):
    def delete(self, request, username):    
        permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        user = User.objects.get(username=username)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
