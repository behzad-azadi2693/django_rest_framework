
from django.contrib.auth.models import User
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
        RetrieveAPIView,ListAPIView,DestroyAPIView, CreateAPIView
    )
from rest_framework.permissions import (
        IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser,
        AllowAny
    )
from .permissions import (
        IsOwnerOrReadOnlyComment, IsOwnerOrReadOnly
)
from .serializer_user import (
    UserDetailSerializer,UserCreateSerializer, UserLoginSerializer
    )

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

class UserLogin(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        data = request.data # this equail with request.POST
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)