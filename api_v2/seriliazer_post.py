from posts.models import Post
from comments.models import Comment
from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from .serializer_comment import CommentSerializer


class PostSerilizer(ModelSerializer):
    user = SerializerMethodField()
    detail_url = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug','image' ,'content', 'publish', 'user', 'detail_url']

    def get_detail_url(self, obj):
        return obj.get_api_url()
    
    def get_user(self, obj):
        return obj.user.username


class PostsSerilizer(ModelSerializer):
    comments = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug','image' ,'content', 'publish', 'user', 'comments']

    def get_comments(self, obj):
        rst = Comment.objects.filter_by_instance(obj)
        return CommentSerializer(instance=rst, many=True).data
    
    def get_user(self, obj):
        return obj.user.username