from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from posts.models import Post
from rest_framework import status, viewsets
from .serializer_post import PostSerilaizer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

'''
request.data --->for access to user submitted data

'''


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def post_list(request):
    if request.method == 'POST':
        info = PostSerilaizer(data=request.data)
        if info.is_valid():
            Post(
                title=validated_data['title'], 
                slug=validated_data['slug'],
                image = validated_data['image'],
                user=request.user
                ).save()

            return Response({'message':'OK'}, status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status = status.HTTP_400_BAD_REQUEST)

    else:#uf request.method == 'GET':
        posts = Post.objects.all()
        srz = PostSerilaizer(posts, many=True).data
        return Response(srz, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated, IsAuthenticatedOrReadOnly])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'erro':'this post dos not exists'})

    srz = PostSerilaizer(post).data
    return Response(srz, status=status.HTTP_200_OK)


class PostViewset(viewsets.ViewSet): #this is controled with routers
    def list(self, request):
        queryset = Post.objects.all()
        srz = PostSerilaizer(queryset, many=True).data
        return Response(srz)

    def retreview(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        srz = PostSerilaizer(post).data
        return Response(srz)

    def create(self, request):
        srz = PostSerilaizer(data=request.data)
        if srz.is_valid():
            srz.save(user=request.user)
            return Response({'message':'OK'})
        else:
            return Response(srz.errors)