from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from posts.models import Post


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
    class Meta:
        model = Post
        fields = ['detail_url', 'title', 'slug', 'content','user', 'destroy_url']


class PostDetailSerializer(ModelSerializer):
    destroy_url = post_destroy_url
    class Meta:
        model = Post
        fields = ['destroy_url', 'id', 'title', 'slug', 'content', 'publish']


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']