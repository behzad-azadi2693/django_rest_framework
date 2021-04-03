from comments.models import Comment
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializer_comment import CommentSerializer


class CommentDetail(APIView):
    def get(self, request,pk):
        comment = Comment.objects.get(pk=pk)
        srz = CommentSerializer(instance=comment).data
        return Response(srz, status=status.HTTP_200_OK)

class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        srz = CommentSerializer(instance=comments, many=True).data
        return Response(srz, status=status.HTTP_200_OK)


class CommentCreate(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        srz = CommentSerializer(data=request.data)
        if srz.is_valid():
            srz.save(user=request.user)
            return Response(srz.data, status=status.HTTP_201_CREATED)
        return Response(srz.error, status=status.HTTP_400_BAD_REQUEST)      


class CommentUpdate(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def put(self, request, pk):
        comment = Vomment.opjects.get(pk=pk)
        self.check_permissions(request, comment)
        srz = CommentSerializer(instance=comment, data=request.data, partial=True)
        if srz.is_valid():
            srz.save(user=request.user)
            return Response(srz.data, status= status.HTTP_200_OK)
        return Response(srz.error, status=status.HTTP_400_BAD_REQUEST)


class CommentDelete(APIView):
    def delete(self, request, pk):    
        permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        comment = Comment.objects.get(pk=pk)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)