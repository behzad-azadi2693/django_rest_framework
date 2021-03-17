from django.shortcuts import render
# Create your views here.
from django.db.models import Q
from posts.models import Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,
    UpdateAPIView,CreateAPIView, RetrieveUpdateDestroyAPIView
    )

from .serializers_post import (
    PostListSerializer, PostDetailSerializer, PostCreateSerializer,
    )

from rest_framework.permissions import (
    AllowAny, IsAdminUser, IsAuthenticated,
    IsAuthenticatedOrReadOnly
    )
#from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


class PostList(ListAPIView):
    #queryset = Post.objects.all() -->1
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]#search for filter backends and ordering for order in url -->&ordering=-title<--
    search_fields = ['title', 'content', 'user__first_name'] # for url while we uses -->/?search=....<-- 
    #pagination_class = LimitOffsetPagination#for usese in url -->/?limit=...<--
    pagination_class = PostLimitOffsetPagination #or PostPageNumberPagination


    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostList, self).get_queryset(*args, **kwargs)  -->1
        #queryse_list = Post.objects.filter(user=self.request.user) --> alone uses
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q') # for url while we uses -->/?p=<--
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__first_name=query)|
                Q(user__last_name=query)
            ).distinct()
        return queryset_list 


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug' #for change default use pk
    #lookup_url_kwarg = 'abc' >>> for change input url --> path('<abc>/', ... ),


class PostDestroy(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug' #for change default use pk
    lookup_url_kwarg = 'abc'
    permission_classes=[IsOwnerOrReadOnly,]


class PostUpdate(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)