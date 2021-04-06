from rest_framework import serializers 
from posts.models import Post

class PostSerilaizer(serializers.Serializer):
    title = serializers.CharField(max_length=150) 
    slug = serializers.SlugField(max_length=200)
    image = serializers.ImageField(allow_null=True)
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(read_only=True)#write_only=True
    

