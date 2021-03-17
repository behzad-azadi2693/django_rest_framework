
from django.contrib.auth.models import User
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.generics import (
        RetrieveAPIView,ListAPIView,DestroyAPIView, CreateAPIView
    )
from rest_framework.permissions import (
        IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser,
    )
from .permissions import (
        IsOwnerOrReadOnlyComment, IsOwnerOrReadOnly
)
from .serializer_user import (
    UserDetailSerializer,UserCreateSerializer
    )

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
