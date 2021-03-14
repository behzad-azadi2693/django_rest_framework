from django.shortcuts import render

# Create your views here.
from posts.models import Post
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, DestroyAPIView,
    UpdateAPIView,CreateAPIView
)
from .serializers import (
    PostListSerializer, PostDetailSerializer, PostCreateSerializer,
    
)

class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


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

class PostUpdate(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)