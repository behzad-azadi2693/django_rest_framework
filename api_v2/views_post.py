from posts.models import Post
from .seriliazer_post import PostSerilizer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class PostDetail(APIView):
    def get(self, request, slug):
        posts = Post.objects.get(slug=slug)
        srz = PostSerilizer(instance=posts, many=True).data
        return Response(srz , status=status.HTTP_200_OK)


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        srz = PostSerilizer(instance=posts, many=True).data
        return Response(srz , status=status.HTTP_200_OK)


class PostCreate(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        data = PostSerilizer(data=request.data)
        if data.is_valid():
            data.save(user=request.user)
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdate(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        srz = PostSerilizer(instance=post, data=request.data,partial=True)
        if srz.is_valid():
            srz.save(user=request.user)
            return Response(srz.data, status=status.HTTP_200_OK)
        return Response(srz.error,status=status.HTTP_400_BAD_REQUEST)


class PostDelete(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
