from rest_framework.generics import (
            ListAPIView, UpdateAPIView, CreateAPIView,
            RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
        )
from rest_framework.permissions import (
            IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly,
            AllowAny
        )
from .serializer_comment import (
            CommentSerializers, CommentChildSerializers, CommentDetailSerializers,
        )        
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from comments.models import Comment
from django.db.models import Q
 

class CommentDetail(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializers


class CommentList(ListAPIView):
    serializer_class = CommentSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination        

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query)|
                Q(user__first_name=query)|
                Q(user__last_name=query)
            ).distinct()
        return queryset_list