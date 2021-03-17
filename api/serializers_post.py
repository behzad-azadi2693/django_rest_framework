from posts.models import Post
from django.contrib.auth.models import User
from .serializer_comment import CommentSerializers
from comments.models import Comment
from .serializer_user import UserDetailSerializer
from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
    )


post_destroy_url = HyperlinkedIdentityField(
        view_name='api:post-destroy',
        lookup_field = 'slug',
        lookup_url_kwarg = 'abc'
    )


class PostListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name = 'api:post-detail',
        lookup_field = 'slug'
        )
    user = SerializerMethodField()
    user_url = HyperlinkedIdentityField(
        view_name='api:user-detail',
        lookup_field = 'user',
        lookup_url_kwarg = 'username'
    )
    class Meta:
        model = Post
        fields = ['detail_url','user_url', 'title', 'content','user']

    def get_user(self, obj):
        return str(obj.user.username)


class PostDetailSerializer(ModelSerializer):
    comments = SerializerMethodField()
    destroy_url = post_destroy_url
    user = UserDetailSerializer()
    image = SerializerMethodField() #this is method just showing not to change
    html = SerializerMethodField()
    user_url = HyperlinkedIdentityField(
        view_name = 'api:user-detail',
        lookup_field = 'user',
        lookup_url_kwarg = 'username',
    )
    class Meta:
        model = Post
        fields = ['destroy_url','user_url', 'id', 'title', 'slug','image' ,'content', 'publish', 'user', 'html', 'comments']

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializers(c_qs, many=True).data
        return comments

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']