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
            CommentListSerializers
        )        
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyComment
from comments.models import Comment
from django.db.models import Q
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin


class CommentList(ListAPIView):
    serializer_class = CommentListSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination        

    
    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.filter(id__gte=0)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query)|
                Q(user__first_name=query)|
                Q(user__last_name=query)
            ).distinct()
        return queryset_list

class CommentEditDetail(UpdateModelMixin,DestroyModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyComment]
    lookup_field ='pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)